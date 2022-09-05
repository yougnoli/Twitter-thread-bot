-- create table: insertion date is default, j column accepts the whole json fromm the pipeline
create table twe.single_json (
	id int identity(1,1) not null primary key
	,j nvarchar(max)
	,insertion_date date default getdate()
)
;
go

select * from twe.single_json
;
go


-- test query to see the final output from the j column
select
	id
	,j
	,convert(date, json_value(j, '$.publication_date')) as publication_date 
	,convert(varchar(5), json_value(j, '$.module')) as modulo
	,convert(varchar(10), json_value(j, '$.page')) as [page]
	,convert(varchar(20), json_value(j, '$.topic')) as topic
	,convert(nvarchar(300), json_value(j, '$.first_tweet')) as first_tweet
	,convert(nvarchar(max), json_value(j, '$.long_tweet')) as long_tweet
from 
	twe.single_json
;
go

-- the output works, I can alter the table and create calculated column
alter table twe.single_json
	add publication_date as convert(date, json_value(j, '$.publication_date'))
	,modulo as convert(varchar(5), json_value(j, '$.module'))
	,[page] as convert(varchar(10), json_value(j, '$.page'))
	,topic as convert(varchar(20), json_value(j, '$.topic')) 
	,first_tweet as convert(nvarchar(300), json_value(j, '$.first_tweet')) 
	,long_tweet as convert(nvarchar(max), json_value(j, '$.long_tweet')) 
;
go

-- test from the python code
select
	first_tweet
	,long_tweet
from twe.single_json
where publication_date = convert(date, getdate())
