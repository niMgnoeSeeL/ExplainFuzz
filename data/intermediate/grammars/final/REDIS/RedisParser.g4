parser grammar RedisParser;

options { tokenVocab=RedisLexer;}

root : commands_question EOF ;

commands_question :  
| command newline_star 
| command newline_plus commands 
| COPY keyName identifier dbclause_question replace_question 
| DEL keyname_plus 
| UNLINK keyname_plus 
| DUMP keyName 
| EXISTS keyname_plus 
| EXPIRE keyName decimal expireoptions_question 
| EXPIREAT keyName decimal expireoptions_question 
| EXPIRETIME keyName 
| PEXPIRE keyName decimal expireoptions_question 
| PEXPIREAT keyName decimal expireoptions_question 
| PEXPIRETIME keyName 
| KEYS keyPattern 
| MOVE keyName databaseName 
| OBJECT objectOptions keyName 
| PERSIST keyName 
| TTL keyName 
| PTTL keyName 
| RANDOMKEY 
| RENAME keyName identifier 
| RENAMENX keyName identifier 
| SCAN decimal matchclause_question countclause_question typeclause_question 
| TOUCH keyname_plus 
| TYPE keyName 
| WAIT POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL 
| SET stringKeyName identifier keyexistenceclause_question get_question block_5_question 
| GET stringKeyName 
| INCR stringKeyName 
| INCRBY stringKeyName decimal 
| DECR stringKeyName 
| DECRBY stringKeyName decimal 
| APPEND stringKeyName identifier 
| GETDEL stringKeyName 
| GETEX stringKeyName block_6_question 
| GETRANGE stringKeyName decimal decimal 
| GETSET stringKeyName identifier 
| MGET stringkeyname_plus 
| MSET block_7_plus 
| MSETNX block_8_plus 
| PSETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| SETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| SETNX stringKeyName identifier 
| SETRANGE stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| STRLEN stringKeyName 
| SUBSTR stringKeyName decimal decimal 
| LMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause 
| BLMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause POSITIVE_DECIMAL_LITERAL 
| LMPOP POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question 
| BLMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question 
| LPOP listKeyName positive_decimal_literal_question 
| BLPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL 
| RPOP listKeyName positive_decimal_literal_question 
| BRPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL 
| RPOPLPUSH listKeyName listKeyName 
| BRPOPLPUSH listKeyName listKeyName POSITIVE_DECIMAL_LITERAL 
| LINDEX listKeyName decimal 
| LINSERT listKeyName beforeOrAfterClause identifier identifier 
| LLEN listKeyName 
| LPOS listKeyName identifier rankclause_question countclause_question maxlenclause_question 
| LPUSH listKeyName identifier_plus 
| LPUSHX listKeyName identifier_plus 
| RPUSH listKeyName identifier_plus 
| RPUSHX listKeyName identifier_plus 
| LRANGE listKeyName decimal decimal 
| LREM listKeyName decimal identifier 
| LSET listKeyName decimal identifier 
| LTRIM listKeyName decimal decimal 
| SADD setKeyName identifier_plus 
| SCARD setKeyName 
| SDIFF setkeyname_plus 
| SDIFFSTORE identifier setkeyname_plus 
| SINTER setkeyname_plus 
| SINTERCARD POSITIVE_DECIMAL_LITERAL setkeyname_plus limitclause_question 
| SINTERSTORE identifier setkeyname_plus 
| SISMEMBER setKeyName identifier 
| SMISMEMBER setKeyName identifier_plus 
| SMEMBERS setKeyName 
| SMOVE setKeyName setKeyName 
| SPOP setKeyName positive_decimal_literal_question 
| SRANDMEMBER setKeyName decimal_question 
| SREM setKeyName identifier_plus 
| SSCAN setKeyName decimal matchclause_question countclause_question 
| SUNION setkeyname_plus 
| SUNIONSTORE identifier setkeyname_plus 
| ZMPOP POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question 
| BZMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question 
| ZPOPMAX sortedSetKeyName positive_decimal_literal_question 
| BZPOPMAX sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL 
| ZPOPMIN sortedSetKeyName positive_decimal_literal_question 
| BZPOPMIN sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL 
| ZADD sortedSetKeyName keyexistenceclause_question keyupdateclause_question ch_question incr_question scorememberclause_plus 
| ZCARD sortedSetKeyName 
| ZCOUNT sortedSetKeyName decimalScore decimalScore 
| ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus withscores_question 
| ZDIFFSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus 
| ZINCRBY sortedSetKeyName decimal identifier 
| ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZINTERCARD POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus limitclause_question 
| ZINTERSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZLEXCOUNT sortedSetKeyName lexicalScore lexicalScore 
| ZSCORE sortedSetKeyName identifier 
| ZMSCORE sortedSetKeyName identifier_plus 
| ZRANDMEMBER sortedSetKeyName block_4_question 
| ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question withscores_question 
| ZRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question 
| ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZRANGESTORE identifier sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question 
| ZRANK sortedSetKeyName identifier withscore_question 
| ZREVRANK sortedSetKeyName identifier withscore_question 
| ZREM sortedSetKeyName identifier_plus 
| ZREMRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore 
| ZREMRANGEBYRANK sortedSetKeyName decimal decimal 
| ZREMRANGEBYSCORE sortedSetKeyName decimalScore decimalScore 
| ZREVRANGE sortedSetKeyName decimal decimal withscores_question 
| ZREVRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question 
| ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZSCAN sortedSetKeyName decimal matchclause_question countclause_question 
| ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZUNIONSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| HDEL hashKeyName identifier_plus 
| HEXISTS hashKeyName identifier 
| HEXPIRE hashKeyName decimal expireoptions_question fieldsClause 
| HPEXPIRE hashKeyName decimal expireoptions_question fieldsClause 
| HEXPIREAT hashKeyName decimal expireoptions_question fieldsClause 
| HPEXPIREAT hashKeyName decimal expireoptions_question fieldsClause 
| HEXPIRETIME hashKeyName fieldsClause 
| HPEXPIRETIME hashKeyName fieldsClause 
| HGET hashKeyName identifier 
| HGETALL hashKeyName 
| HINCRBY hashKeyName identifier decimal 
| HKEYS hashKeyName 
| HLEN hashKeyName 
| HMGET hashKeyName identifier_plus 
| HSET hashKeyName block_0_plus 
| HMSET hashKeyName block_1_plus 
| HSETNX hashKeyName identifier identifier 
| HPERSIST hashKeyName fieldsClause 
| HTTL hashKeyName fieldsClause 
| HPTTL hashKeyName fieldsClause 
| HRANDFIELD hashKeyName block_2_question 
| HSCAN hashKeyName decimal matchclause_question countclause_question novalues_question 
| HSTRLEN hashKeyName identifier 
| HVALS hashKeyName 
| ZREVRANGE sortedSetKeyName decimal decimal 
| ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question 
| ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question 
| ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus 
| ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question 
| ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question ;

commands : command newline_star 
| command newline_plus commands 
| COPY keyName identifier dbclause_question replace_question 
| DEL keyname_plus 
| UNLINK keyname_plus 
| DUMP keyName 
| EXISTS keyname_plus 
| EXPIRE keyName decimal expireoptions_question 
| EXPIREAT keyName decimal expireoptions_question 
| EXPIRETIME keyName 
| PEXPIRE keyName decimal expireoptions_question 
| PEXPIREAT keyName decimal expireoptions_question 
| PEXPIRETIME keyName 
| KEYS keyPattern 
| MOVE keyName databaseName 
| OBJECT objectOptions keyName 
| PERSIST keyName 
| TTL keyName 
| PTTL keyName 
| RANDOMKEY 
| RENAME keyName identifier 
| RENAMENX keyName identifier 
| SCAN decimal matchclause_question countclause_question typeclause_question 
| TOUCH keyname_plus 
| TYPE keyName 
| WAIT POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL 
| SET stringKeyName identifier keyexistenceclause_question get_question block_5_question 
| GET stringKeyName 
| INCR stringKeyName 
| INCRBY stringKeyName decimal 
| DECR stringKeyName 
| DECRBY stringKeyName decimal 
| APPEND stringKeyName identifier 
| GETDEL stringKeyName 
| GETEX stringKeyName block_6_question 
| GETRANGE stringKeyName decimal decimal 
| GETSET stringKeyName identifier 
| MGET stringkeyname_plus 
| MSET block_7_plus 
| MSETNX block_8_plus 
| PSETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| SETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| SETNX stringKeyName identifier 
| SETRANGE stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| STRLEN stringKeyName 
| SUBSTR stringKeyName decimal decimal 
| LMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause 
| BLMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause POSITIVE_DECIMAL_LITERAL 
| LMPOP POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question 
| BLMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question 
| LPOP listKeyName positive_decimal_literal_question 
| BLPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL 
| RPOP listKeyName positive_decimal_literal_question 
| BRPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL 
| RPOPLPUSH listKeyName listKeyName 
| BRPOPLPUSH listKeyName listKeyName POSITIVE_DECIMAL_LITERAL 
| LINDEX listKeyName decimal 
| LINSERT listKeyName beforeOrAfterClause identifier identifier 
| LLEN listKeyName 
| LPOS listKeyName identifier rankclause_question countclause_question maxlenclause_question 
| LPUSH listKeyName identifier_plus 
| LPUSHX listKeyName identifier_plus 
| RPUSH listKeyName identifier_plus 
| RPUSHX listKeyName identifier_plus 
| LRANGE listKeyName decimal decimal 
| LREM listKeyName decimal identifier 
| LSET listKeyName decimal identifier 
| LTRIM listKeyName decimal decimal 
| SADD setKeyName identifier_plus 
| SCARD setKeyName 
| SDIFF setkeyname_plus 
| SDIFFSTORE identifier setkeyname_plus 
| SINTER setkeyname_plus 
| SINTERCARD POSITIVE_DECIMAL_LITERAL setkeyname_plus limitclause_question 
| SINTERSTORE identifier setkeyname_plus 
| SISMEMBER setKeyName identifier 
| SMISMEMBER setKeyName identifier_plus 
| SMEMBERS setKeyName 
| SMOVE setKeyName setKeyName 
| SPOP setKeyName positive_decimal_literal_question 
| SRANDMEMBER setKeyName decimal_question 
| SREM setKeyName identifier_plus 
| SSCAN setKeyName decimal matchclause_question countclause_question 
| SUNION setkeyname_plus 
| SUNIONSTORE identifier setkeyname_plus 
| ZMPOP POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question 
| BZMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question 
| ZPOPMAX sortedSetKeyName positive_decimal_literal_question 
| BZPOPMAX sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL 
| ZPOPMIN sortedSetKeyName positive_decimal_literal_question 
| BZPOPMIN sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL 
| ZADD sortedSetKeyName keyexistenceclause_question keyupdateclause_question ch_question incr_question scorememberclause_plus 
| ZCARD sortedSetKeyName 
| ZCOUNT sortedSetKeyName decimalScore decimalScore 
| ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus withscores_question 
| ZDIFFSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus 
| ZINCRBY sortedSetKeyName decimal identifier 
| ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZINTERCARD POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus limitclause_question 
| ZINTERSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZLEXCOUNT sortedSetKeyName lexicalScore lexicalScore 
| ZSCORE sortedSetKeyName identifier 
| ZMSCORE sortedSetKeyName identifier_plus 
| ZRANDMEMBER sortedSetKeyName block_4_question 
| ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question withscores_question 
| ZRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question 
| ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZRANGESTORE identifier sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question 
| ZRANK sortedSetKeyName identifier withscore_question 
| ZREVRANK sortedSetKeyName identifier withscore_question 
| ZREM sortedSetKeyName identifier_plus 
| ZREMRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore 
| ZREMRANGEBYRANK sortedSetKeyName decimal decimal 
| ZREMRANGEBYSCORE sortedSetKeyName decimalScore decimalScore 
| ZREVRANGE sortedSetKeyName decimal decimal withscores_question 
| ZREVRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question 
| ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZSCAN sortedSetKeyName decimal matchclause_question countclause_question 
| ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZUNIONSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| HDEL hashKeyName identifier_plus 
| HEXISTS hashKeyName identifier 
| HEXPIRE hashKeyName decimal expireoptions_question fieldsClause 
| HPEXPIRE hashKeyName decimal expireoptions_question fieldsClause 
| HEXPIREAT hashKeyName decimal expireoptions_question fieldsClause 
| HPEXPIREAT hashKeyName decimal expireoptions_question fieldsClause 
| HEXPIRETIME hashKeyName fieldsClause 
| HPEXPIRETIME hashKeyName fieldsClause 
| HGET hashKeyName identifier 
| HGETALL hashKeyName 
| HINCRBY hashKeyName identifier decimal 
| HKEYS hashKeyName 
| HLEN hashKeyName 
| HMGET hashKeyName identifier_plus 
| HSET hashKeyName block_0_plus 
| HMSET hashKeyName block_1_plus 
| HSETNX hashKeyName identifier identifier 
| HPERSIST hashKeyName fieldsClause 
| HTTL hashKeyName fieldsClause 
| HPTTL hashKeyName fieldsClause 
| HRANDFIELD hashKeyName block_2_question 
| HSCAN hashKeyName decimal matchclause_question countclause_question novalues_question 
| HSTRLEN hashKeyName identifier 
| HVALS hashKeyName 
| ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question 
| ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZREVRANGE sortedSetKeyName decimal decimal 
| ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question 
| ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question 
| ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus ;

newline_plus : NEWLINE newline_plus 
| NEWLINE ;

newline_star : NEWLINE newline_star 
| NEWLINE ;

hdelCommand : HDEL hashKeyName identifier_plus ;

identifier_plus : identifier identifier_plus 
| IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

hexistsCommand : HEXISTS hashKeyName identifier ;

hexpireCommand : HEXPIRE hashKeyName decimal expireoptions_question fieldsClause ;

expireoptions_question :  
| NX 
| XX 
| GT 
| LT ;

hpexpireCommand : HPEXPIRE hashKeyName decimal expireoptions_question fieldsClause ;

fieldsClause : FIELDS POSITIVE_DECIMAL_LITERAL identifier_plus ;

hexpireAtCommand : HEXPIREAT hashKeyName decimal expireoptions_question fieldsClause ;

hpexpireAtCommand : HPEXPIREAT hashKeyName decimal expireoptions_question fieldsClause ;

hexpireTimeCommand : HEXPIRETIME hashKeyName fieldsClause ;

hpexpireTimeCommand : HPEXPIRETIME hashKeyName fieldsClause ;

hgetCommand : HGET hashKeyName identifier ;

hmgetCommand : HMGET hashKeyName identifier_plus ;

hgetAllCommand : HGETALL hashKeyName ;

hincrByCommand : HINCRBY hashKeyName identifier decimal ;

hkeysCommand : HKEYS hashKeyName ;

hlenCommand : HLEN hashKeyName ;

block_0 : identifier identifier ;

hsetCommand : HSET hashKeyName block_0_plus ;

block_0_plus : block_0 block_0_plus 
| identifier identifier ;

block_1 : identifier identifier ;

hmsetCommand : HMSET hashKeyName block_1_plus ;

block_1_plus : block_1 block_1_plus 
| identifier identifier ;

hsetnxCommand : HSETNX hashKeyName identifier identifier ;

hpersistCommand : HPERSIST hashKeyName fieldsClause ;

httlCommand : HTTL hashKeyName fieldsClause ;

hpttlCommand : HPTTL hashKeyName fieldsClause ;

block_2 : decimal withvalues_question 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_LITERAL ;

withvalues_question : WITHVALUES ;

hrandfieldCommand : HRANDFIELD hashKeyName block_2_question ;

block_2_question :  
| decimal withvalues_question 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_LITERAL ;

hscanCommand : HSCAN hashKeyName decimal matchclause_question countclause_question novalues_question ;

novalues_question : NOVALUES 
|  ;

countclause_question :  
| COUNT POSITIVE_DECIMAL_LITERAL ;

matchclause_question :  
| MATCH keyPattern ;

hstrlenCommand : HSTRLEN hashKeyName identifier ;

hvalsCommand : HVALS hashKeyName ;

zmpopCommand : ZMPOP POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question ;

sortedsetkeyname_plus : sortedSetKeyName sortedsetkeyname_plus 
| IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

bzmpopCommand : BZMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question ;

zpopmaxCommand : ZPOPMAX sortedSetKeyName positive_decimal_literal_question ;

positive_decimal_literal_question : POSITIVE_DECIMAL_LITERAL 
|  ;

bzpopmaxCommand : BZPOPMAX sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL ;

zpopminCommand : ZPOPMIN sortedSetKeyName positive_decimal_literal_question ;

bzpopminCommand : BZPOPMIN sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL ;

minMaxClause : MIN 
| MAX ;

zaddCommand : ZADD sortedSetKeyName keyexistenceclause_question keyupdateclause_question ch_question incr_question scorememberclause_plus ;

scorememberclause_plus : scoreMemberClause scorememberclause_plus 
| decimal identifier ;

incr_question : INCR 
|  ;

ch_question : CH 
|  ;

keyupdateclause_question :  
| GT 
| LT ;

keyexistenceclause_question :  
| NX 
| XX ;

keyUpdateClause : GT 
| LT ;

scoreMemberClause : decimal identifier ;

zcardCommand : ZCARD sortedSetKeyName ;

zcountCommand : ZCOUNT sortedSetKeyName decimalScore decimalScore ;

zdiffCommand : ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus withscores_question 
| ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus ;

withscores_question : WITHSCORES ;

zdiffstoreCommand : ZDIFFSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus ;

zincrbyCommand : ZINCRBY sortedSetKeyName decimal identifier ;

zinterCommand : ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question ;

aggregateclause_question :  
| AGGREGATE block_3 ;

weightsclause_question :  
| WEIGHTS decimal_plus ;

zintercardCommand : ZINTERCARD POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus limitclause_question ;

limitclause_question :  
| LIMIT POSITIVE_DECIMAL_LITERAL ;

zinterstoreCommand : ZINTERSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question ;

weightsClause : WEIGHTS decimal_plus ;

decimal_plus : decimal decimal_plus 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_LITERAL ;

block_3 : MIN 
| MAX 
| SUM ;

aggregateClause : AGGREGATE block_3 ;

zlexcountCommand : ZLEXCOUNT sortedSetKeyName lexicalScore lexicalScore ;

zscoreCommand : ZSCORE sortedSetKeyName identifier ;

zmscoreCommand : ZMSCORE sortedSetKeyName identifier_plus ;

block_4 : decimal withscores_question 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_LITERAL ;

zrandmemberCommand : ZRANDMEMBER sortedSetKeyName block_4_question ;

block_4_question :  
| decimal withscores_question 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_LITERAL ;

zrangeCommand : ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question withscores_question 
| ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question ;

limitoffsetclause_question :  
| LIMIT decimal decimal ;

rev_question : REV 
|  ;

rangetypeclause_question :  
| BYSCORE 
| BYLEX ;

zrangebylexCommand : ZRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question ;

zrangebyscoreCommand : ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question ;

zrangestoreCommand : ZRANGESTORE identifier sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question ;

rangeTypeClause : BYSCORE 
| BYLEX ;

limitOffsetClause : LIMIT decimal decimal ;

zrankCommand : ZRANK sortedSetKeyName identifier withscore_question ;

withscore_question : WITHSCORE 
|  ;

zrevrankCommand : ZREVRANK sortedSetKeyName identifier withscore_question ;

zremCommand : ZREM sortedSetKeyName identifier_plus ;

zremrangebylexCommand : ZREMRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore ;

zremrangebyrankCommand : ZREMRANGEBYRANK sortedSetKeyName decimal decimal ;

zremrangebyscoreCommand : ZREMRANGEBYSCORE sortedSetKeyName decimalScore decimalScore ;

zrevrangeCommand : ZREVRANGE sortedSetKeyName decimal decimal withscores_question 
| ZREVRANGE sortedSetKeyName decimal decimal ;

zrevrangebylexCommand : ZREVRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question ;

zrevrangebyscoreCommand : ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question ;

zscanCommand : ZSCAN sortedSetKeyName decimal matchclause_question countclause_question ;

zunionCommand : ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question ;

zunionstoreCommand : ZUNIONSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question ;

saddCommand : SADD setKeyName identifier_plus ;

scardCommand : SCARD setKeyName ;

sdiffCommand : SDIFF setkeyname_plus ;

setkeyname_plus : setKeyName setkeyname_plus 
| IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

sdiffstoreCommand : SDIFFSTORE identifier setkeyname_plus ;

sinterCommand : SINTER setkeyname_plus ;

sintercardCommand : SINTERCARD POSITIVE_DECIMAL_LITERAL setkeyname_plus limitclause_question ;

limitClause : LIMIT POSITIVE_DECIMAL_LITERAL ;

sinterstoreCommand : SINTERSTORE identifier setkeyname_plus ;

sismemberCommand : SISMEMBER setKeyName identifier ;

smismemberCommand : SMISMEMBER setKeyName identifier_plus ;

smembersCommand : SMEMBERS setKeyName ;

smoveCommand : SMOVE setKeyName setKeyName ;

spopCommand : SPOP setKeyName positive_decimal_literal_question ;

srandmemberCommand : SRANDMEMBER setKeyName decimal_question ;

decimal_question :  
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_LITERAL ;

sremCommand : SREM setKeyName identifier_plus ;

sscanComman : SSCAN setKeyName decimal matchclause_question countclause_question ;

sunionCommand : SUNION setkeyname_plus ;

sunionstoreCommand : SUNIONSTORE identifier setkeyname_plus ;

lmoveCommand : LMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause ;

leftOrRightClause : LEFT 
| RIGHT ;

blmoveCommand : BLMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause POSITIVE_DECIMAL_LITERAL ;

lmpopCommand : LMPOP POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question ;

listkeyname_plus : listKeyName listkeyname_plus 
| IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

blmpopCommand : BLMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question ;

lpopCommand : LPOP listKeyName positive_decimal_literal_question ;

blpopCommand : BLPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL ;

rpopCommand : RPOP listKeyName positive_decimal_literal_question ;

brpopCommand : BRPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL ;

rpopLpushCommand : RPOPLPUSH listKeyName listKeyName ;

brpopLpushCommand : BRPOPLPUSH listKeyName listKeyName POSITIVE_DECIMAL_LITERAL ;

lindexCommand : LINDEX listKeyName decimal ;

linsertCommand : LINSERT listKeyName beforeOrAfterClause identifier identifier ;

beforeOrAfterClause : BEFORE 
| AFTER ;

llenCommand : LLEN listKeyName ;

lposCommand : LPOS listKeyName identifier rankclause_question countclause_question maxlenclause_question ;

maxlenclause_question :  
| MAXLEN POSITIVE_DECIMAL_LITERAL ;

rankclause_question :  
| RANK decimal ;

rankClause : RANK decimal ;

maxLenClause : MAXLEN POSITIVE_DECIMAL_LITERAL ;

lpushCommand : LPUSH listKeyName identifier_plus ;

lpushxCommand : LPUSHX listKeyName identifier_plus ;

rpushCommand : RPUSH listKeyName identifier_plus ;

rpushxCommand : RPUSHX listKeyName identifier_plus ;

lrangeCommand : LRANGE listKeyName decimal decimal ;

lremCommand : LREM listKeyName decimal identifier ;

lsetCommand : LSET listKeyName decimal identifier ;

ltrimCommand : LTRIM listKeyName decimal decimal ;

copyCommand : COPY keyName identifier dbclause_question replace_question ;

replace_question : REPLACE 
|  ;

dbclause_question :  
| DB databaseName ;

dbClause : DB databaseName ;

databaseName : POSITIVE_DECIMAL_LITERAL ;

deleteCommand : DEL keyname_plus ;

keyname_plus : keyName keyname_plus 
| IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

unlinkCommand : UNLINK keyname_plus ;

dumpCommand : DUMP keyName ;

existsCommand : EXISTS keyname_plus ;

expireCommand : EXPIRE keyName decimal expireoptions_question ;

expireAtCommand : EXPIREAT keyName decimal expireoptions_question ;

pExpireCommand : PEXPIRE keyName decimal expireoptions_question ;

pExpireAtCommand : PEXPIREAT keyName decimal expireoptions_question ;

expireOptions : NX 
| XX 
| GT 
| LT ;

expireTimeCommand : EXPIRETIME keyName ;

pExpireTimeCommand : PEXPIRETIME keyName ;

keysCommand : KEYS keyPattern ;

moveCommand : MOVE keyName databaseName ;

objectCommand : OBJECT objectOptions keyName ;

objectOptions : ENCODING 
| FREQ 
| IDLETIME 
| REFCOUNT ;

persistCommand : PERSIST keyName ;

ttlCommand : TTL keyName ;

pTtlCommand : PTTL keyName ;

randomKeyCommand : RANDOMKEY ;

renameCommand : RENAME keyName identifier ;

renameNxCommand : RENAMENX keyName identifier ;

scanCommand : SCAN decimal matchclause_question countclause_question typeclause_question ;

typeclause_question :  
| TYPE identifier ;

matchClause : MATCH keyPattern ;

countClause : COUNT POSITIVE_DECIMAL_LITERAL ;

typeClause : TYPE identifier ;

touchCommand : TOUCH keyname_plus ;

typeCommand : TYPE keyName ;

waitCommand : WAIT POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL ;

block_5 : KEEPTTL 
| EX POSITIVE_DECIMAL_LITERAL 
| PX POSITIVE_DECIMAL_LITERAL 
| EXAT POSITIVE_DECIMAL_LITERAL 
| PXAT POSITIVE_DECIMAL_LITERAL ;

stringSetCommand : SET stringKeyName identifier keyexistenceclause_question get_question block_5_question ;

block_5_question :  
| KEEPTTL 
| EX POSITIVE_DECIMAL_LITERAL 
| PX POSITIVE_DECIMAL_LITERAL 
| EXAT POSITIVE_DECIMAL_LITERAL 
| PXAT POSITIVE_DECIMAL_LITERAL ;

get_question : GET 
|  ;

keyExistenceClause : NX 
| XX ;

expirationClause : EX POSITIVE_DECIMAL_LITERAL 
| PX POSITIVE_DECIMAL_LITERAL 
| EXAT POSITIVE_DECIMAL_LITERAL 
| PXAT POSITIVE_DECIMAL_LITERAL ;

getCommand : GET stringKeyName ;

incrementCommand : INCR stringKeyName ;

incrementByCommand : INCRBY stringKeyName decimal ;

decrementCommand : DECR stringKeyName ;

decrementByCommand : DECRBY stringKeyName decimal ;

appendCommand : APPEND stringKeyName identifier ;

getDeleteCommand : GETDEL stringKeyName ;

block_6 : PERSIST 
| EX POSITIVE_DECIMAL_LITERAL 
| PX POSITIVE_DECIMAL_LITERAL 
| EXAT POSITIVE_DECIMAL_LITERAL 
| PXAT POSITIVE_DECIMAL_LITERAL ;

getExCommand : GETEX stringKeyName block_6_question ;

block_6_question :  
| PERSIST 
| EX POSITIVE_DECIMAL_LITERAL 
| PX POSITIVE_DECIMAL_LITERAL 
| EXAT POSITIVE_DECIMAL_LITERAL 
| PXAT POSITIVE_DECIMAL_LITERAL ;

getRangeCommand : GETRANGE stringKeyName decimal decimal ;

getSetCommand : GETSET stringKeyName identifier ;

mGetCommand : MGET stringkeyname_plus ;

stringkeyname_plus : stringKeyName stringkeyname_plus 
| IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

block_7 : stringKeyName identifier ;

mSetCommand : MSET block_7_plus ;

block_7_plus : block_7 block_7_plus 
| stringKeyName identifier ;

block_8 : stringKeyName identifier ;

mSetNxCommand : MSETNX block_8_plus ;

block_8_plus : block_8 block_8_plus 
| stringKeyName identifier ;

pSetExCommand : PSETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier ;

setExCommand : SETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier ;

setNxCommand : SETNX stringKeyName identifier ;

setRangeCommand : SETRANGE stringKeyName POSITIVE_DECIMAL_LITERAL identifier ;

stringLengthCommand : STRLEN stringKeyName ;

substringCommand : SUBSTR stringKeyName decimal decimal ;

decimal : POSITIVE_DECIMAL_LITERAL 
| DECIMAL_LITERAL ;

decimalScore : POSITIVE_DECIMAL_LITERAL 
| DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

identifier : IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

commonCommand : COPY keyName identifier dbclause_question replace_question 
| DEL keyname_plus 
| UNLINK keyname_plus 
| DUMP keyName 
| EXISTS keyname_plus 
| EXPIRE keyName decimal expireoptions_question 
| EXPIREAT keyName decimal expireoptions_question 
| EXPIRETIME keyName 
| PEXPIRE keyName decimal expireoptions_question 
| PEXPIREAT keyName decimal expireoptions_question 
| PEXPIRETIME keyName 
| KEYS keyPattern 
| MOVE keyName databaseName 
| OBJECT objectOptions keyName 
| PERSIST keyName 
| TTL keyName 
| PTTL keyName 
| RANDOMKEY 
| RENAME keyName identifier 
| RENAMENX keyName identifier 
| SCAN decimal matchclause_question countclause_question typeclause_question 
| TOUCH keyname_plus 
| TYPE keyName 
| WAIT POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL ;

stringCommand : SET stringKeyName identifier keyexistenceclause_question get_question block_5_question 
| GET stringKeyName 
| INCR stringKeyName 
| INCRBY stringKeyName decimal 
| DECR stringKeyName 
| DECRBY stringKeyName decimal 
| APPEND stringKeyName identifier 
| GETDEL stringKeyName 
| GETEX stringKeyName block_6_question 
| GETRANGE stringKeyName decimal decimal 
| GETSET stringKeyName identifier 
| MGET stringkeyname_plus 
| MSET block_7_plus 
| MSETNX block_8_plus 
| PSETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| SETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| SETNX stringKeyName identifier 
| SETRANGE stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| STRLEN stringKeyName 
| SUBSTR stringKeyName decimal decimal ;

listCommand : LMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause 
| BLMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause POSITIVE_DECIMAL_LITERAL 
| LMPOP POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question 
| BLMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question 
| LPOP listKeyName positive_decimal_literal_question 
| BLPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL 
| RPOP listKeyName positive_decimal_literal_question 
| BRPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL 
| RPOPLPUSH listKeyName listKeyName 
| BRPOPLPUSH listKeyName listKeyName POSITIVE_DECIMAL_LITERAL 
| LINDEX listKeyName decimal 
| LINSERT listKeyName beforeOrAfterClause identifier identifier 
| LLEN listKeyName 
| LPOS listKeyName identifier rankclause_question countclause_question maxlenclause_question 
| LPUSH listKeyName identifier_plus 
| LPUSHX listKeyName identifier_plus 
| RPUSH listKeyName identifier_plus 
| RPUSHX listKeyName identifier_plus 
| LRANGE listKeyName decimal decimal 
| LREM listKeyName decimal identifier 
| LSET listKeyName decimal identifier 
| LTRIM listKeyName decimal decimal ;

setCommand : SADD setKeyName identifier_plus 
| SCARD setKeyName 
| SDIFF setkeyname_plus 
| SDIFFSTORE identifier setkeyname_plus 
| SINTER setkeyname_plus 
| SINTERCARD POSITIVE_DECIMAL_LITERAL setkeyname_plus limitclause_question 
| SINTERSTORE identifier setkeyname_plus 
| SISMEMBER setKeyName identifier 
| SMISMEMBER setKeyName identifier_plus 
| SMEMBERS setKeyName 
| SMOVE setKeyName setKeyName 
| SPOP setKeyName positive_decimal_literal_question 
| SRANDMEMBER setKeyName decimal_question 
| SREM setKeyName identifier_plus 
| SSCAN setKeyName decimal matchclause_question countclause_question 
| SUNION setkeyname_plus 
| SUNIONSTORE identifier setkeyname_plus ;

sortedSetCommand : ZMPOP POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question 
| BZMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question 
| ZPOPMAX sortedSetKeyName positive_decimal_literal_question 
| BZPOPMAX sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL 
| ZPOPMIN sortedSetKeyName positive_decimal_literal_question 
| BZPOPMIN sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL 
| ZADD sortedSetKeyName keyexistenceclause_question keyupdateclause_question ch_question incr_question scorememberclause_plus 
| ZCARD sortedSetKeyName 
| ZCOUNT sortedSetKeyName decimalScore decimalScore 
| ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus withscores_question 
| ZDIFFSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus 
| ZINCRBY sortedSetKeyName decimal identifier 
| ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZINTERCARD POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus limitclause_question 
| ZINTERSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZLEXCOUNT sortedSetKeyName lexicalScore lexicalScore 
| ZSCORE sortedSetKeyName identifier 
| ZMSCORE sortedSetKeyName identifier_plus 
| ZRANDMEMBER sortedSetKeyName block_4_question 
| ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question withscores_question 
| ZRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question 
| ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZRANGESTORE identifier sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question 
| ZRANK sortedSetKeyName identifier withscore_question 
| ZREVRANK sortedSetKeyName identifier withscore_question 
| ZREM sortedSetKeyName identifier_plus 
| ZREMRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore 
| ZREMRANGEBYRANK sortedSetKeyName decimal decimal 
| ZREMRANGEBYSCORE sortedSetKeyName decimalScore decimalScore 
| ZREVRANGE sortedSetKeyName decimal decimal withscores_question 
| ZREVRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question 
| ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZSCAN sortedSetKeyName decimal matchclause_question countclause_question 
| ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZUNIONSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus 
| ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question 
| ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZREVRANGE sortedSetKeyName decimal decimal 
| ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question 
| ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question 
| ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question ;

hashCommand : HDEL hashKeyName identifier_plus 
| HEXISTS hashKeyName identifier 
| HEXPIRE hashKeyName decimal expireoptions_question fieldsClause 
| HPEXPIRE hashKeyName decimal expireoptions_question fieldsClause 
| HEXPIREAT hashKeyName decimal expireoptions_question fieldsClause 
| HPEXPIREAT hashKeyName decimal expireoptions_question fieldsClause 
| HEXPIRETIME hashKeyName fieldsClause 
| HPEXPIRETIME hashKeyName fieldsClause 
| HGET hashKeyName identifier 
| HGETALL hashKeyName 
| HINCRBY hashKeyName identifier decimal 
| HKEYS hashKeyName 
| HLEN hashKeyName 
| HMGET hashKeyName identifier_plus 
| HSET hashKeyName block_0_plus 
| HMSET hashKeyName block_1_plus 
| HSETNX hashKeyName identifier identifier 
| HPERSIST hashKeyName fieldsClause 
| HTTL hashKeyName fieldsClause 
| HPTTL hashKeyName fieldsClause 
| HRANDFIELD hashKeyName block_2_question 
| HSCAN hashKeyName decimal matchclause_question countclause_question novalues_question 
| HSTRLEN hashKeyName identifier 
| HVALS hashKeyName ;

lexicalScore : IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

stringKeyName : IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

listKeyName : IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

setKeyName : IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

sortedSetKeyName : IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

hashKeyName : IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

keyName : IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

keyPattern : IDENTIFIER 
| DECIMAL_LITERAL 
| POSITIVE_DECIMAL_LITERAL 
| DECIMAL_SCORE_LITERAL ;

command : COPY keyName identifier dbclause_question replace_question 
| DEL keyname_plus 
| UNLINK keyname_plus 
| DUMP keyName 
| EXISTS keyname_plus 
| EXPIRE keyName decimal expireoptions_question 
| EXPIREAT keyName decimal expireoptions_question 
| EXPIRETIME keyName 
| PEXPIRE keyName decimal expireoptions_question 
| PEXPIREAT keyName decimal expireoptions_question 
| PEXPIRETIME keyName 
| KEYS keyPattern 
| MOVE keyName databaseName 
| OBJECT objectOptions keyName 
| PERSIST keyName 
| TTL keyName 
| PTTL keyName 
| RANDOMKEY 
| RENAME keyName identifier 
| RENAMENX keyName identifier 
| SCAN decimal matchclause_question countclause_question typeclause_question 
| TOUCH keyname_plus 
| TYPE keyName 
| WAIT POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL 
| SET stringKeyName identifier keyexistenceclause_question get_question block_5_question 
| GET stringKeyName 
| INCR stringKeyName 
| INCRBY stringKeyName decimal 
| DECR stringKeyName 
| DECRBY stringKeyName decimal 
| APPEND stringKeyName identifier 
| GETDEL stringKeyName 
| GETEX stringKeyName block_6_question 
| GETRANGE stringKeyName decimal decimal 
| GETSET stringKeyName identifier 
| MGET stringkeyname_plus 
| MSET block_7_plus 
| MSETNX block_8_plus 
| PSETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| SETEX stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| SETNX stringKeyName identifier 
| SETRANGE stringKeyName POSITIVE_DECIMAL_LITERAL identifier 
| STRLEN stringKeyName 
| SUBSTR stringKeyName decimal decimal 
| LMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause 
| BLMOVE listKeyName listKeyName leftOrRightClause leftOrRightClause POSITIVE_DECIMAL_LITERAL 
| LMPOP POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question 
| BLMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL listkeyname_plus leftOrRightClause countclause_question 
| LPOP listKeyName positive_decimal_literal_question 
| BLPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL 
| RPOP listKeyName positive_decimal_literal_question 
| BRPOP listkeyname_plus POSITIVE_DECIMAL_LITERAL 
| RPOPLPUSH listKeyName listKeyName 
| BRPOPLPUSH listKeyName listKeyName POSITIVE_DECIMAL_LITERAL 
| LINDEX listKeyName decimal 
| LINSERT listKeyName beforeOrAfterClause identifier identifier 
| LLEN listKeyName 
| LPOS listKeyName identifier rankclause_question countclause_question maxlenclause_question 
| LPUSH listKeyName identifier_plus 
| LPUSHX listKeyName identifier_plus 
| RPUSH listKeyName identifier_plus 
| RPUSHX listKeyName identifier_plus 
| LRANGE listKeyName decimal decimal 
| LREM listKeyName decimal identifier 
| LSET listKeyName decimal identifier 
| LTRIM listKeyName decimal decimal 
| SADD setKeyName identifier_plus 
| SCARD setKeyName 
| SDIFF setkeyname_plus 
| SDIFFSTORE identifier setkeyname_plus 
| SINTER setkeyname_plus 
| SINTERCARD POSITIVE_DECIMAL_LITERAL setkeyname_plus limitclause_question 
| SINTERSTORE identifier setkeyname_plus 
| SISMEMBER setKeyName identifier 
| SMISMEMBER setKeyName identifier_plus 
| SMEMBERS setKeyName 
| SMOVE setKeyName setKeyName 
| SPOP setKeyName positive_decimal_literal_question 
| SRANDMEMBER setKeyName decimal_question 
| SREM setKeyName identifier_plus 
| SSCAN setKeyName decimal matchclause_question countclause_question 
| SUNION setkeyname_plus 
| SUNIONSTORE identifier setkeyname_plus 
| ZMPOP POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question 
| BZMPOP POSITIVE_DECIMAL_LITERAL POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus minMaxClause countclause_question 
| ZPOPMAX sortedSetKeyName positive_decimal_literal_question 
| BZPOPMAX sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL 
| ZPOPMIN sortedSetKeyName positive_decimal_literal_question 
| BZPOPMIN sortedsetkeyname_plus POSITIVE_DECIMAL_LITERAL 
| ZADD sortedSetKeyName keyexistenceclause_question keyupdateclause_question ch_question incr_question scorememberclause_plus 
| ZCARD sortedSetKeyName 
| ZCOUNT sortedSetKeyName decimalScore decimalScore 
| ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus withscores_question 
| ZDIFFSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus 
| ZINCRBY sortedSetKeyName decimal identifier 
| ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZINTERCARD POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus limitclause_question 
| ZINTERSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZLEXCOUNT sortedSetKeyName lexicalScore lexicalScore 
| ZSCORE sortedSetKeyName identifier 
| ZMSCORE sortedSetKeyName identifier_plus 
| ZRANDMEMBER sortedSetKeyName block_4_question 
| ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question withscores_question 
| ZRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question 
| ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZRANGESTORE identifier sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question 
| ZRANK sortedSetKeyName identifier withscore_question 
| ZREVRANK sortedSetKeyName identifier withscore_question 
| ZREM sortedSetKeyName identifier_plus 
| ZREMRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore 
| ZREMRANGEBYRANK sortedSetKeyName decimal decimal 
| ZREMRANGEBYSCORE sortedSetKeyName decimalScore decimalScore 
| ZREVRANGE sortedSetKeyName decimal decimal withscores_question 
| ZREVRANGEBYLEX sortedSetKeyName lexicalScore lexicalScore limitoffsetclause_question 
| ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore withscores_question limitoffsetclause_question 
| ZSCAN sortedSetKeyName decimal matchclause_question countclause_question 
| ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question withscores_question 
| ZUNIONSTORE identifier POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| HDEL hashKeyName identifier_plus 
| HEXISTS hashKeyName identifier 
| HEXPIRE hashKeyName decimal expireoptions_question fieldsClause 
| HPEXPIRE hashKeyName decimal expireoptions_question fieldsClause 
| HEXPIREAT hashKeyName decimal expireoptions_question fieldsClause 
| HPEXPIREAT hashKeyName decimal expireoptions_question fieldsClause 
| HEXPIRETIME hashKeyName fieldsClause 
| HPEXPIRETIME hashKeyName fieldsClause 
| HGET hashKeyName identifier 
| HGETALL hashKeyName 
| HINCRBY hashKeyName identifier decimal 
| HKEYS hashKeyName 
| HLEN hashKeyName 
| HMGET hashKeyName identifier_plus 
| HSET hashKeyName block_0_plus 
| HMSET hashKeyName block_1_plus 
| HSETNX hashKeyName identifier identifier 
| HPERSIST hashKeyName fieldsClause 
| HTTL hashKeyName fieldsClause 
| HPTTL hashKeyName fieldsClause 
| HRANDFIELD hashKeyName block_2_question 
| HSCAN hashKeyName decimal matchclause_question countclause_question novalues_question 
| HSTRLEN hashKeyName identifier 
| HVALS hashKeyName 
| ZRANGE sortedSetKeyName lexicalScore lexicalScore rangetypeclause_question rev_question limitoffsetclause_question 
| ZUNION POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZDIFF POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus 
| ZINTER POSITIVE_DECIMAL_LITERAL sortedsetkeyname_plus weightsclause_question aggregateclause_question 
| ZRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question 
| ZREVRANGE sortedSetKeyName decimal decimal 
| ZREVRANGEBYSCORE sortedSetKeyName decimalScore decimalScore limitoffsetclause_question ;

