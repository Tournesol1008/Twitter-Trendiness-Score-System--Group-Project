CREATE OR REPLACE TABLE t (obj jsonb);

insert into t (obj)
select
    regexp_split_to_table(
        replace(v, $$"}{"$$, $$"}djue748wBc,l;09{"$$),
        'djue748wBc,l;09'
    )::jsonb
from (

) s;

COPY t from '///home/gb760/Group5-760/tweet_json_file.json';
 select values->>'created_at' as CreationDate,
       values->>'id' as userid,
       values->>'lang' as lang,
       values->>'text' as text     
  from(
          select json_array_elements(values) as values 
          from tweet_import
  ) a;



CREATE ORc REPLACE TABLE Tweets(
   CreationDate timestamp NOT NULL,
   userid integer NOT NULL,
   lang varchar(255) NOT NULL,
   text integer NOT NULL,
   CONSTRAINT id_pk PRIMARY KEY (userid)
);

