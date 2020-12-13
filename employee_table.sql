
--create table department (Deptid int primary key, dep_Description varchar(100) , dept_status Varchar(1))

/*
create table addresss (addressid int primary key, type_of_address varchar(50), 
addline1 varchar(100) , addline2 varchar(100) , Landmark varchar(50), District varchar(50), 
state_ varchar(50), country varchar(50), Pincode int, add_status char(1)) */


/*create table branch (Branchid int primary key, branch_desc varchar(100) , addressid int , 
branch_status char(1),foreign key (addressid) references addresss(addressid))*/

/*create table designation (designationId int primary key , designation_description varchar(100), designation_status char(1),
Branchid int foreign key(branchid) references branch(Branchid))*/

/*create table professional (professionalid int primary key, Doj datetime , dor datetime , designation varchar(100), 
companyname varchar(100) , proffession_Address varchar(100) ,  salary int)


create table contact (contactid int primary key , emailid varchar(50) , phoneno int , alternatephoneno varchar(50))*/



/*create table personal (personalid int primary key, firstname varchar(50), lastname varchar(50) , dob datetime , maritalstatus varchar(50), 
aadharid int , voterid int , pancardno int , gender varchar(10) , professionalid int foreign key (professionalid) references professional(professionalid), 
passportno int , passportvalid date , addressid int foreign key (addressid) references addresss(addressid))*/


/*create table employee (empid int primary key , firstname varchar(50), lastname varchar(50) , salary float(20),
deptid int foreign key (deptid) references department(deptid), managerid int , addressid int foreign key (addressid) references addresss(addressid)
, designationid int foreign key (designationid) references designation (designationId) , professionalid int foreign key (professionalid) references professional (professionalid),
branchid int foreign key (branchid) references branch(branchid), personalid int foreign key (personalid) references personal(personalid) , 
contactid int foreign key (contactid) references contact(contactid))*/

/*Alter table contact  alter column alternatephoneno int

Alter table professional alter column Doj date

Alter table professional alter column dor date

Alter table department alter column dept_status char(1)


Alter table employee add created_by varchar(50),created_datetime datetime,  modified_by varchar(50) , modified_datetime datetime

Alter table branch add created_by varchar(50),created_datetime datetime,  modified_by varchar(50) , modified_datetime datetime

Alter table addresss add created_by varchar(50),created_datetime datetime,  modified_by varchar(50) , modified_datetime datetime

Alter table designation add created_by varchar(50),created_datetime datetime,modified_by varchar(50) , modified_datetime datetime

Alter table department add created_by varchar(50),created_datetime datetime,modified_by varchar(50) , modified_datetime datetime

Alter table professional add created_by varchar(50),created_datetime datetime,modified_by varchar(50) , modified_datetime datetime

Alter table contact add created_by varchar(50),created_datetime datetime,modified_by varchar(50) , modified_datetime datetime


Alter table personal add created_by varchar(50),created_datetime datetime,modified_by varchar(50) , modified_datetime datetime */



/*Alter table branch alter column branch_desc varchar(100) Not null

alter table designa
Alter table professional alter column Doj date not null
Alter table professional alter column dor date not nulltion alter column designation_description varchar(100) not null


Alter table department alter column dep_description varchar(100) not null


Alter table addresss add constraint typeofadderess_constraint
check (type_of_address in ('Permanent','Current'))*/


Alter table addresss add constraint Status_constraint
check (add_status in ('Y','N'))



Alter table designation add constraint Status_designation_constraint
check (designation_status in ('Y','N'))


Alter table department add constraint status_dept_contraint
check (dept_status in ('Y','N'))

Alter table personal add constraint maritalstatus_constraint
check (maritalstatus in ('Single','Married','Divorce','Widow'))

Alter table personal add constraint gender_constraint
check (Gender in ('Male','Female','Other'))

Alter table branch add constraint status_Branch_constraint
check (branch_status in ('Y','N'))

Alter table professional
drop CONSTRAINT PK__professi__A7355D67435ADFAB

ALTER TABLE EMPLOYEE
DROP CONSTRAINT FK__employee__profes__5FB337D6

Alter table personal
drop constraint FK__personal__profes__44FF419A


Alter table professional
add constraint pk_profession primary key (professionalid,Doj)

Alter table designation
add constraint designation_default default ('N') for designation_status

Alter table department
add constraint dept_default_status default ('N') for dept_status

Alter table branch
add constraint branch_default_status default ('N') for branch_status



