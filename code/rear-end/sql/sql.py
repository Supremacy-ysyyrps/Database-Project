sql_del = """
reset role;

revoke all on table Product, PurchaseRecord, SalesRecord, Inventory from buyer;
revoke all on table Product, PurchaseRecord, SalesRecord, Inventory from seller;
drop role buyer, seller;

drop trigger T1 on Product;
drop trigger T2 on PurchaseRecord;
drop trigger T3 on PurchaseRecord;
drop trigger T4 on SalesRecord;
drop trigger T5 on SalesRecord;

drop table PurchaseRecord, SalesRecord, Inventory, Product;
"""

sql_init = """
create table Product(
    P_ID int primary key,
    P_Name varchar(30),
    P_Type varchar(30));
create table PurchaseRecord(
    PR_ID int primary key,
    P_ID int references Product(P_ID) on delete cascade,
    PR_Num int,
    PR_UnitPrice float,
    PR_Date date);
create table SalesRecord(
    SR_ID int primary key,
    P_ID int references Product(P_ID) on delete cascade,
    SR_Num int,
    SR_UnitPrice float,
    SR_Date date);
create table Inventory(
    P_ID int primary key references Product(P_ID) on delete cascade,
    I_CurStock int,
    I_MaxStock int,
    I_MinStock int);

create or replace function add_product() returns trigger as
    $$
        begin
            insert into Inventory
            values(new.P_ID, 0, 200, 0);
            return null;
        end;
    $$ language plpgsql;
create trigger T1 after insert on Product
    for each row
    execute function add_product();

create or replace function add_purchase() returns trigger as
    $$
        begin
            update Inventory
            set I_Curstock = I_Curstock + new.PR_Num
            where P_ID = new.P_ID;
            return null;
        end
    $$ language plpgsql;
create trigger T2 after insert on PurchaseRecord
    for each row
    execute function add_purchase();

create or replace function del_purchase() returns trigger as
    $$
        begin
            update Inventory
            set I_Curstock = I_Curstock - old.PR_Num
            where P_ID = old.P_ID;
            return null;
        end
    $$ language plpgsql;
create trigger T3 after delete on PurchaseRecord
    for each row
    execute function del_purchase();

create or replace function add_sales() returns trigger as
    $$
        begin
            update Inventory
            set I_Curstock = I_Curstock - new.SR_Num
            where P_ID = new.P_ID;
            return null;
        end
    $$ language plpgsql;
create trigger T4 after insert on SalesRecord
    for each row
    execute function add_sales();

create or replace function del_sales() returns trigger as
    $$
        begin
            update Inventory
            set I_Curstock = I_Curstock + old.SR_Num
            where P_ID = old.P_ID;
            return null;
        end
    $$ language plpgsql;
create trigger T5 after delete on SalesRecord
    for each row
    execute function del_sales();

create or replace function capacity_limitation() returns trigger as
    $$
        begin
            if new.I_Curstock > new.I_Maxstock then
                raise exception '容量不足';
            elseif new.I_Curstock < new.I_Minstock then
                raise exception '库存不足';
            end if;
            return new;
        end
    $$ language plpgsql;
create trigger T6 before update on Inventory
    for each row
    execute function capacity_limitation();

create role buyer;
create role seller;
grant select on table Product, SalesRecord, Inventory to buyer;
grant update on table Inventory to buyer;
grant all on table PurchaseRecord to buyer;
grant select on table Product, PurchaseRecord, Inventory to seller;
grant update on table Inventory to seller;
grant all on table SalesRecord to seller;
"""

sql_rebuild = sql_del + sql_init

sql_insert_product = """
-- 向 Product 表插入20条记录
insert into Product (P_ID, P_Name, P_Type) VALUES
(1, 'Orange', 'Fruit'),
(2, 'Eggs', 'Dairy'),
(3, 'Cereal', 'Breakfast'),
(4, 'Beef', 'Meat'),
(5, 'Soap', 'Personal Care'),
(6, 'Monitor', 'Electronics'),
(7, 'Grapes', 'Fruit'),
(8, 'Cheese', 'Dairy'),
(9, 'Conditioner', 'Personal Care'),
(10, 'Cucumber', 'Vegetable'),
(11, 'Banana', 'Fruit'),
(12, 'Butter', 'Dairy'),
(13, 'Juice', 'Beverage'),
(14, 'Pork', 'Meat'),
(15, 'Toilet Paper', 'Household'),
(16, 'Printer', 'Electronics'),
(17, 'Strawberries', 'Fruit'),
(18, 'Yogurt Drink', 'Dairy'),
(19, 'Toothbrush', 'Personal Care'),
(20, 'Carrot', 'Vegetable');
"""

sql_insert_purchaserecord = """
-- 向 PurchaseRecord 表插入20条记录
insert into PurchaseRecord (PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date) VALUES
(1, 1, 60, 1.8, '2023-02-01'),
(2, 2, 40, 1.2, '2023-02-02'),
(3, 3, 25, 4.5, '2023-02-03'),
(4, 4, 90, 2.0, '2023-02-04'),
(5, 5, 30, 3.0, '2023-02-05'),
(6, 6, 75, 1.5, '2023-02-06'),
(7, 7, 20, 2.8, '2023-02-07'),
(8, 8, 35, 1.0, '2023-02-08'),
(9, 9, 50, 2.5, '2023-02-09'),
(10, 10, 60, 1.7, '2023-02-10'),
(11, 11, 70, 1.6, '2023-02-11'),
(12, 12, 55, 2.3, '2023-02-12'),
(13, 13, 60, 1.9, '2023-02-13'),
(14, 14, 40, 2.2, '2023-02-14'),
(15, 15, 60, 3.5, '2023-02-15'),
(16, 16, 20, 1.5, '2023-02-16'),
(17, 17, 20, 5.0, '2023-02-17'),
(18, 18, 10, 120.0, '2023-02-18'),
(19, 19, 20, 3.2, '2023-02-19'),
(20, 20, 25, 2.0, '2023-02-20');
"""

sql_insert_salesrecord = """
-- 向 SalesRecord 表插入20条记录
insert into SalesRecord (SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date) VALUES
(1, 1, 30, 2.0, '2023-02-21'),
(2, 2, 20, 4.0, '2023-02-22'),
(3, 3, 3, 2.5, '2023-02-23'),
(4, 4, 15, 1.8, '2023-02-24'),
(5, 5, 20, 3.2, '2023-02-25'),
(6, 6, 50, 1.3, '2023-02-26'),
(7, 7, 5, 3.0, '2023-02-27'),
(8, 8, 10, 1.0, '2023-02-28'),
(9, 9, 22, 2.2, '2023-03-01'),
(10, 10, 8, 1.5, '2023-03-02'),
(11, 11, 10, 1.3, '2023-03-03'),
(12, 12, 15, 4.2, '2023-03-04'),
(13, 13, 20, 150.0, '2023-03-05'),
(14, 14, 18, 3.0, '2023-03-06'),
(15, 15, 28, 1.6, '2023-03-07'),
(16, 16, 8, 2.8, '2023-03-08'),
(17, 17, 12, 5.5, '2023-03-09'),
(18, 18, 4, 180.0, '2023-03-10'),
(19, 19, 18, 1.9, '2023-03-11'),
(20, 20, 15, 1.2, '2023-03-12');
"""

sql_insert_all = [
    sql_insert_product,
    sql_insert_purchaserecord,
    sql_insert_salesrecord,
]

sql_select_product = """
select * from Product order by P_ID;
"""

sql_select_purchaserecord = """
select * from PurchaseRecord order by P_ID, PR_ID;
"""

sql_select_salesrecord = """
select * from SalesRecord order by P_ID, SR_ID;
"""

sql_select_inventory = """
select * from Inventory order by P_ID;
"""

sql_select_all = [
    sql_select_product,
    sql_select_purchaserecord,
    sql_select_salesrecord,
    sql_select_inventory
]