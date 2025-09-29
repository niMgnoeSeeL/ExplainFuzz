# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/REDIS/RedisParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .RedisParser import RedisParser
else:
    from RedisParser import RedisParser

# This class defines a complete listener for a parse tree produced by RedisParser.
class RedisParserListener(ParseTreeListener):

    # Enter a parse tree produced by RedisParser#root.
    def enterRoot(self, ctx:RedisParser.RootContext):
        pass

    # Exit a parse tree produced by RedisParser#root.
    def exitRoot(self, ctx:RedisParser.RootContext):
        pass


    # Enter a parse tree produced by RedisParser#commands.
    def enterCommands(self, ctx:RedisParser.CommandsContext):
        pass

    # Exit a parse tree produced by RedisParser#commands.
    def exitCommands(self, ctx:RedisParser.CommandsContext):
        pass


    # Enter a parse tree produced by RedisParser#command.
    def enterCommand(self, ctx:RedisParser.CommandContext):
        pass

    # Exit a parse tree produced by RedisParser#command.
    def exitCommand(self, ctx:RedisParser.CommandContext):
        pass


    # Enter a parse tree produced by RedisParser#commonCommand.
    def enterCommonCommand(self, ctx:RedisParser.CommonCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#commonCommand.
    def exitCommonCommand(self, ctx:RedisParser.CommonCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#stringCommand.
    def enterStringCommand(self, ctx:RedisParser.StringCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#stringCommand.
    def exitStringCommand(self, ctx:RedisParser.StringCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#listCommand.
    def enterListCommand(self, ctx:RedisParser.ListCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#listCommand.
    def exitListCommand(self, ctx:RedisParser.ListCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#setCommand.
    def enterSetCommand(self, ctx:RedisParser.SetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#setCommand.
    def exitSetCommand(self, ctx:RedisParser.SetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#sortedSetCommand.
    def enterSortedSetCommand(self, ctx:RedisParser.SortedSetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sortedSetCommand.
    def exitSortedSetCommand(self, ctx:RedisParser.SortedSetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hashCommand.
    def enterHashCommand(self, ctx:RedisParser.HashCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hashCommand.
    def exitHashCommand(self, ctx:RedisParser.HashCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hdelCommand.
    def enterHdelCommand(self, ctx:RedisParser.HdelCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hdelCommand.
    def exitHdelCommand(self, ctx:RedisParser.HdelCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hexistsCommand.
    def enterHexistsCommand(self, ctx:RedisParser.HexistsCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hexistsCommand.
    def exitHexistsCommand(self, ctx:RedisParser.HexistsCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hexpireCommand.
    def enterHexpireCommand(self, ctx:RedisParser.HexpireCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hexpireCommand.
    def exitHexpireCommand(self, ctx:RedisParser.HexpireCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hpexpireCommand.
    def enterHpexpireCommand(self, ctx:RedisParser.HpexpireCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hpexpireCommand.
    def exitHpexpireCommand(self, ctx:RedisParser.HpexpireCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#fieldsClause.
    def enterFieldsClause(self, ctx:RedisParser.FieldsClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#fieldsClause.
    def exitFieldsClause(self, ctx:RedisParser.FieldsClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#hexpireAtCommand.
    def enterHexpireAtCommand(self, ctx:RedisParser.HexpireAtCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hexpireAtCommand.
    def exitHexpireAtCommand(self, ctx:RedisParser.HexpireAtCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hpexpireAtCommand.
    def enterHpexpireAtCommand(self, ctx:RedisParser.HpexpireAtCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hpexpireAtCommand.
    def exitHpexpireAtCommand(self, ctx:RedisParser.HpexpireAtCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hexpireTimeCommand.
    def enterHexpireTimeCommand(self, ctx:RedisParser.HexpireTimeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hexpireTimeCommand.
    def exitHexpireTimeCommand(self, ctx:RedisParser.HexpireTimeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hpexpireTimeCommand.
    def enterHpexpireTimeCommand(self, ctx:RedisParser.HpexpireTimeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hpexpireTimeCommand.
    def exitHpexpireTimeCommand(self, ctx:RedisParser.HpexpireTimeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hgetCommand.
    def enterHgetCommand(self, ctx:RedisParser.HgetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hgetCommand.
    def exitHgetCommand(self, ctx:RedisParser.HgetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hmgetCommand.
    def enterHmgetCommand(self, ctx:RedisParser.HmgetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hmgetCommand.
    def exitHmgetCommand(self, ctx:RedisParser.HmgetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hgetAllCommand.
    def enterHgetAllCommand(self, ctx:RedisParser.HgetAllCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hgetAllCommand.
    def exitHgetAllCommand(self, ctx:RedisParser.HgetAllCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hincrByCommand.
    def enterHincrByCommand(self, ctx:RedisParser.HincrByCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hincrByCommand.
    def exitHincrByCommand(self, ctx:RedisParser.HincrByCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hkeysCommand.
    def enterHkeysCommand(self, ctx:RedisParser.HkeysCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hkeysCommand.
    def exitHkeysCommand(self, ctx:RedisParser.HkeysCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hlenCommand.
    def enterHlenCommand(self, ctx:RedisParser.HlenCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hlenCommand.
    def exitHlenCommand(self, ctx:RedisParser.HlenCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hsetCommand.
    def enterHsetCommand(self, ctx:RedisParser.HsetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hsetCommand.
    def exitHsetCommand(self, ctx:RedisParser.HsetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hmsetCommand.
    def enterHmsetCommand(self, ctx:RedisParser.HmsetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hmsetCommand.
    def exitHmsetCommand(self, ctx:RedisParser.HmsetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hsetnxCommand.
    def enterHsetnxCommand(self, ctx:RedisParser.HsetnxCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hsetnxCommand.
    def exitHsetnxCommand(self, ctx:RedisParser.HsetnxCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hpersistCommand.
    def enterHpersistCommand(self, ctx:RedisParser.HpersistCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hpersistCommand.
    def exitHpersistCommand(self, ctx:RedisParser.HpersistCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#httlCommand.
    def enterHttlCommand(self, ctx:RedisParser.HttlCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#httlCommand.
    def exitHttlCommand(self, ctx:RedisParser.HttlCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hpttlCommand.
    def enterHpttlCommand(self, ctx:RedisParser.HpttlCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hpttlCommand.
    def exitHpttlCommand(self, ctx:RedisParser.HpttlCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hrandfieldCommand.
    def enterHrandfieldCommand(self, ctx:RedisParser.HrandfieldCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hrandfieldCommand.
    def exitHrandfieldCommand(self, ctx:RedisParser.HrandfieldCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hscanCommand.
    def enterHscanCommand(self, ctx:RedisParser.HscanCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hscanCommand.
    def exitHscanCommand(self, ctx:RedisParser.HscanCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hstrlenCommand.
    def enterHstrlenCommand(self, ctx:RedisParser.HstrlenCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hstrlenCommand.
    def exitHstrlenCommand(self, ctx:RedisParser.HstrlenCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#hvalsCommand.
    def enterHvalsCommand(self, ctx:RedisParser.HvalsCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#hvalsCommand.
    def exitHvalsCommand(self, ctx:RedisParser.HvalsCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zmpopCommand.
    def enterZmpopCommand(self, ctx:RedisParser.ZmpopCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zmpopCommand.
    def exitZmpopCommand(self, ctx:RedisParser.ZmpopCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#bzmpopCommand.
    def enterBzmpopCommand(self, ctx:RedisParser.BzmpopCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#bzmpopCommand.
    def exitBzmpopCommand(self, ctx:RedisParser.BzmpopCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zpopmaxCommand.
    def enterZpopmaxCommand(self, ctx:RedisParser.ZpopmaxCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zpopmaxCommand.
    def exitZpopmaxCommand(self, ctx:RedisParser.ZpopmaxCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#bzpopmaxCommand.
    def enterBzpopmaxCommand(self, ctx:RedisParser.BzpopmaxCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#bzpopmaxCommand.
    def exitBzpopmaxCommand(self, ctx:RedisParser.BzpopmaxCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zpopminCommand.
    def enterZpopminCommand(self, ctx:RedisParser.ZpopminCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zpopminCommand.
    def exitZpopminCommand(self, ctx:RedisParser.ZpopminCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#bzpopminCommand.
    def enterBzpopminCommand(self, ctx:RedisParser.BzpopminCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#bzpopminCommand.
    def exitBzpopminCommand(self, ctx:RedisParser.BzpopminCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#minMaxClause.
    def enterMinMaxClause(self, ctx:RedisParser.MinMaxClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#minMaxClause.
    def exitMinMaxClause(self, ctx:RedisParser.MinMaxClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#zaddCommand.
    def enterZaddCommand(self, ctx:RedisParser.ZaddCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zaddCommand.
    def exitZaddCommand(self, ctx:RedisParser.ZaddCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#keyUpdateClause.
    def enterKeyUpdateClause(self, ctx:RedisParser.KeyUpdateClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#keyUpdateClause.
    def exitKeyUpdateClause(self, ctx:RedisParser.KeyUpdateClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#scoreMemberClause.
    def enterScoreMemberClause(self, ctx:RedisParser.ScoreMemberClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#scoreMemberClause.
    def exitScoreMemberClause(self, ctx:RedisParser.ScoreMemberClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#zcardCommand.
    def enterZcardCommand(self, ctx:RedisParser.ZcardCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zcardCommand.
    def exitZcardCommand(self, ctx:RedisParser.ZcardCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zcountCommand.
    def enterZcountCommand(self, ctx:RedisParser.ZcountCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zcountCommand.
    def exitZcountCommand(self, ctx:RedisParser.ZcountCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zdiffCommand.
    def enterZdiffCommand(self, ctx:RedisParser.ZdiffCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zdiffCommand.
    def exitZdiffCommand(self, ctx:RedisParser.ZdiffCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zdiffstoreCommand.
    def enterZdiffstoreCommand(self, ctx:RedisParser.ZdiffstoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zdiffstoreCommand.
    def exitZdiffstoreCommand(self, ctx:RedisParser.ZdiffstoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zincrbyCommand.
    def enterZincrbyCommand(self, ctx:RedisParser.ZincrbyCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zincrbyCommand.
    def exitZincrbyCommand(self, ctx:RedisParser.ZincrbyCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zinterCommand.
    def enterZinterCommand(self, ctx:RedisParser.ZinterCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zinterCommand.
    def exitZinterCommand(self, ctx:RedisParser.ZinterCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zintercardCommand.
    def enterZintercardCommand(self, ctx:RedisParser.ZintercardCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zintercardCommand.
    def exitZintercardCommand(self, ctx:RedisParser.ZintercardCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zinterstoreCommand.
    def enterZinterstoreCommand(self, ctx:RedisParser.ZinterstoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zinterstoreCommand.
    def exitZinterstoreCommand(self, ctx:RedisParser.ZinterstoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#weightsClause.
    def enterWeightsClause(self, ctx:RedisParser.WeightsClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#weightsClause.
    def exitWeightsClause(self, ctx:RedisParser.WeightsClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#aggregateClause.
    def enterAggregateClause(self, ctx:RedisParser.AggregateClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#aggregateClause.
    def exitAggregateClause(self, ctx:RedisParser.AggregateClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#zlexcountCommand.
    def enterZlexcountCommand(self, ctx:RedisParser.ZlexcountCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zlexcountCommand.
    def exitZlexcountCommand(self, ctx:RedisParser.ZlexcountCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zscoreCommand.
    def enterZscoreCommand(self, ctx:RedisParser.ZscoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zscoreCommand.
    def exitZscoreCommand(self, ctx:RedisParser.ZscoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zmscoreCommand.
    def enterZmscoreCommand(self, ctx:RedisParser.ZmscoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zmscoreCommand.
    def exitZmscoreCommand(self, ctx:RedisParser.ZmscoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zrandmemberCommand.
    def enterZrandmemberCommand(self, ctx:RedisParser.ZrandmemberCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrandmemberCommand.
    def exitZrandmemberCommand(self, ctx:RedisParser.ZrandmemberCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zrangeCommand.
    def enterZrangeCommand(self, ctx:RedisParser.ZrangeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrangeCommand.
    def exitZrangeCommand(self, ctx:RedisParser.ZrangeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zrangebylexCommand.
    def enterZrangebylexCommand(self, ctx:RedisParser.ZrangebylexCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrangebylexCommand.
    def exitZrangebylexCommand(self, ctx:RedisParser.ZrangebylexCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zrangebyscoreCommand.
    def enterZrangebyscoreCommand(self, ctx:RedisParser.ZrangebyscoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrangebyscoreCommand.
    def exitZrangebyscoreCommand(self, ctx:RedisParser.ZrangebyscoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zrangestoreCommand.
    def enterZrangestoreCommand(self, ctx:RedisParser.ZrangestoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrangestoreCommand.
    def exitZrangestoreCommand(self, ctx:RedisParser.ZrangestoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#rangeTypeClause.
    def enterRangeTypeClause(self, ctx:RedisParser.RangeTypeClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#rangeTypeClause.
    def exitRangeTypeClause(self, ctx:RedisParser.RangeTypeClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#limitOffsetClause.
    def enterLimitOffsetClause(self, ctx:RedisParser.LimitOffsetClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#limitOffsetClause.
    def exitLimitOffsetClause(self, ctx:RedisParser.LimitOffsetClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#zrankCommand.
    def enterZrankCommand(self, ctx:RedisParser.ZrankCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrankCommand.
    def exitZrankCommand(self, ctx:RedisParser.ZrankCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zrevrankCommand.
    def enterZrevrankCommand(self, ctx:RedisParser.ZrevrankCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrevrankCommand.
    def exitZrevrankCommand(self, ctx:RedisParser.ZrevrankCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zremCommand.
    def enterZremCommand(self, ctx:RedisParser.ZremCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zremCommand.
    def exitZremCommand(self, ctx:RedisParser.ZremCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zremrangebylexCommand.
    def enterZremrangebylexCommand(self, ctx:RedisParser.ZremrangebylexCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zremrangebylexCommand.
    def exitZremrangebylexCommand(self, ctx:RedisParser.ZremrangebylexCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zremrangebyrankCommand.
    def enterZremrangebyrankCommand(self, ctx:RedisParser.ZremrangebyrankCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zremrangebyrankCommand.
    def exitZremrangebyrankCommand(self, ctx:RedisParser.ZremrangebyrankCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zremrangebyscoreCommand.
    def enterZremrangebyscoreCommand(self, ctx:RedisParser.ZremrangebyscoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zremrangebyscoreCommand.
    def exitZremrangebyscoreCommand(self, ctx:RedisParser.ZremrangebyscoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zrevrangeCommand.
    def enterZrevrangeCommand(self, ctx:RedisParser.ZrevrangeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrevrangeCommand.
    def exitZrevrangeCommand(self, ctx:RedisParser.ZrevrangeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zrevrangebylexCommand.
    def enterZrevrangebylexCommand(self, ctx:RedisParser.ZrevrangebylexCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrevrangebylexCommand.
    def exitZrevrangebylexCommand(self, ctx:RedisParser.ZrevrangebylexCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zrevrangebyscoreCommand.
    def enterZrevrangebyscoreCommand(self, ctx:RedisParser.ZrevrangebyscoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zrevrangebyscoreCommand.
    def exitZrevrangebyscoreCommand(self, ctx:RedisParser.ZrevrangebyscoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zscanCommand.
    def enterZscanCommand(self, ctx:RedisParser.ZscanCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zscanCommand.
    def exitZscanCommand(self, ctx:RedisParser.ZscanCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zunionCommand.
    def enterZunionCommand(self, ctx:RedisParser.ZunionCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zunionCommand.
    def exitZunionCommand(self, ctx:RedisParser.ZunionCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#zunionstoreCommand.
    def enterZunionstoreCommand(self, ctx:RedisParser.ZunionstoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#zunionstoreCommand.
    def exitZunionstoreCommand(self, ctx:RedisParser.ZunionstoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#saddCommand.
    def enterSaddCommand(self, ctx:RedisParser.SaddCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#saddCommand.
    def exitSaddCommand(self, ctx:RedisParser.SaddCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#scardCommand.
    def enterScardCommand(self, ctx:RedisParser.ScardCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#scardCommand.
    def exitScardCommand(self, ctx:RedisParser.ScardCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#sdiffCommand.
    def enterSdiffCommand(self, ctx:RedisParser.SdiffCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sdiffCommand.
    def exitSdiffCommand(self, ctx:RedisParser.SdiffCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#sdiffstoreCommand.
    def enterSdiffstoreCommand(self, ctx:RedisParser.SdiffstoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sdiffstoreCommand.
    def exitSdiffstoreCommand(self, ctx:RedisParser.SdiffstoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#sinterCommand.
    def enterSinterCommand(self, ctx:RedisParser.SinterCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sinterCommand.
    def exitSinterCommand(self, ctx:RedisParser.SinterCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#sintercardCommand.
    def enterSintercardCommand(self, ctx:RedisParser.SintercardCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sintercardCommand.
    def exitSintercardCommand(self, ctx:RedisParser.SintercardCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#limitClause.
    def enterLimitClause(self, ctx:RedisParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#limitClause.
    def exitLimitClause(self, ctx:RedisParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#sinterstoreCommand.
    def enterSinterstoreCommand(self, ctx:RedisParser.SinterstoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sinterstoreCommand.
    def exitSinterstoreCommand(self, ctx:RedisParser.SinterstoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#sismemberCommand.
    def enterSismemberCommand(self, ctx:RedisParser.SismemberCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sismemberCommand.
    def exitSismemberCommand(self, ctx:RedisParser.SismemberCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#smismemberCommand.
    def enterSmismemberCommand(self, ctx:RedisParser.SmismemberCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#smismemberCommand.
    def exitSmismemberCommand(self, ctx:RedisParser.SmismemberCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#smembersCommand.
    def enterSmembersCommand(self, ctx:RedisParser.SmembersCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#smembersCommand.
    def exitSmembersCommand(self, ctx:RedisParser.SmembersCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#smoveCommand.
    def enterSmoveCommand(self, ctx:RedisParser.SmoveCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#smoveCommand.
    def exitSmoveCommand(self, ctx:RedisParser.SmoveCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#spopCommand.
    def enterSpopCommand(self, ctx:RedisParser.SpopCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#spopCommand.
    def exitSpopCommand(self, ctx:RedisParser.SpopCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#srandmemberCommand.
    def enterSrandmemberCommand(self, ctx:RedisParser.SrandmemberCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#srandmemberCommand.
    def exitSrandmemberCommand(self, ctx:RedisParser.SrandmemberCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#sremCommand.
    def enterSremCommand(self, ctx:RedisParser.SremCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sremCommand.
    def exitSremCommand(self, ctx:RedisParser.SremCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#sscanComman.
    def enterSscanComman(self, ctx:RedisParser.SscanCommanContext):
        pass

    # Exit a parse tree produced by RedisParser#sscanComman.
    def exitSscanComman(self, ctx:RedisParser.SscanCommanContext):
        pass


    # Enter a parse tree produced by RedisParser#sunionCommand.
    def enterSunionCommand(self, ctx:RedisParser.SunionCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sunionCommand.
    def exitSunionCommand(self, ctx:RedisParser.SunionCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#sunionstoreCommand.
    def enterSunionstoreCommand(self, ctx:RedisParser.SunionstoreCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#sunionstoreCommand.
    def exitSunionstoreCommand(self, ctx:RedisParser.SunionstoreCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#lmoveCommand.
    def enterLmoveCommand(self, ctx:RedisParser.LmoveCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lmoveCommand.
    def exitLmoveCommand(self, ctx:RedisParser.LmoveCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#leftOrRightClause.
    def enterLeftOrRightClause(self, ctx:RedisParser.LeftOrRightClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#leftOrRightClause.
    def exitLeftOrRightClause(self, ctx:RedisParser.LeftOrRightClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#blmoveCommand.
    def enterBlmoveCommand(self, ctx:RedisParser.BlmoveCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#blmoveCommand.
    def exitBlmoveCommand(self, ctx:RedisParser.BlmoveCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#lmpopCommand.
    def enterLmpopCommand(self, ctx:RedisParser.LmpopCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lmpopCommand.
    def exitLmpopCommand(self, ctx:RedisParser.LmpopCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#blmpopCommand.
    def enterBlmpopCommand(self, ctx:RedisParser.BlmpopCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#blmpopCommand.
    def exitBlmpopCommand(self, ctx:RedisParser.BlmpopCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#lpopCommand.
    def enterLpopCommand(self, ctx:RedisParser.LpopCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lpopCommand.
    def exitLpopCommand(self, ctx:RedisParser.LpopCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#blpopCommand.
    def enterBlpopCommand(self, ctx:RedisParser.BlpopCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#blpopCommand.
    def exitBlpopCommand(self, ctx:RedisParser.BlpopCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#rpopCommand.
    def enterRpopCommand(self, ctx:RedisParser.RpopCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#rpopCommand.
    def exitRpopCommand(self, ctx:RedisParser.RpopCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#brpopCommand.
    def enterBrpopCommand(self, ctx:RedisParser.BrpopCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#brpopCommand.
    def exitBrpopCommand(self, ctx:RedisParser.BrpopCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#rpopLpushCommand.
    def enterRpopLpushCommand(self, ctx:RedisParser.RpopLpushCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#rpopLpushCommand.
    def exitRpopLpushCommand(self, ctx:RedisParser.RpopLpushCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#brpopLpushCommand.
    def enterBrpopLpushCommand(self, ctx:RedisParser.BrpopLpushCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#brpopLpushCommand.
    def exitBrpopLpushCommand(self, ctx:RedisParser.BrpopLpushCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#lindexCommand.
    def enterLindexCommand(self, ctx:RedisParser.LindexCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lindexCommand.
    def exitLindexCommand(self, ctx:RedisParser.LindexCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#linsertCommand.
    def enterLinsertCommand(self, ctx:RedisParser.LinsertCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#linsertCommand.
    def exitLinsertCommand(self, ctx:RedisParser.LinsertCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#beforeOrAfterClause.
    def enterBeforeOrAfterClause(self, ctx:RedisParser.BeforeOrAfterClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#beforeOrAfterClause.
    def exitBeforeOrAfterClause(self, ctx:RedisParser.BeforeOrAfterClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#llenCommand.
    def enterLlenCommand(self, ctx:RedisParser.LlenCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#llenCommand.
    def exitLlenCommand(self, ctx:RedisParser.LlenCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#lposCommand.
    def enterLposCommand(self, ctx:RedisParser.LposCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lposCommand.
    def exitLposCommand(self, ctx:RedisParser.LposCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#rankClause.
    def enterRankClause(self, ctx:RedisParser.RankClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#rankClause.
    def exitRankClause(self, ctx:RedisParser.RankClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#maxLenClause.
    def enterMaxLenClause(self, ctx:RedisParser.MaxLenClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#maxLenClause.
    def exitMaxLenClause(self, ctx:RedisParser.MaxLenClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#lpushCommand.
    def enterLpushCommand(self, ctx:RedisParser.LpushCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lpushCommand.
    def exitLpushCommand(self, ctx:RedisParser.LpushCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#lpushxCommand.
    def enterLpushxCommand(self, ctx:RedisParser.LpushxCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lpushxCommand.
    def exitLpushxCommand(self, ctx:RedisParser.LpushxCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#rpushCommand.
    def enterRpushCommand(self, ctx:RedisParser.RpushCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#rpushCommand.
    def exitRpushCommand(self, ctx:RedisParser.RpushCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#rpushxCommand.
    def enterRpushxCommand(self, ctx:RedisParser.RpushxCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#rpushxCommand.
    def exitRpushxCommand(self, ctx:RedisParser.RpushxCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#lrangeCommand.
    def enterLrangeCommand(self, ctx:RedisParser.LrangeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lrangeCommand.
    def exitLrangeCommand(self, ctx:RedisParser.LrangeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#lremCommand.
    def enterLremCommand(self, ctx:RedisParser.LremCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lremCommand.
    def exitLremCommand(self, ctx:RedisParser.LremCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#lsetCommand.
    def enterLsetCommand(self, ctx:RedisParser.LsetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#lsetCommand.
    def exitLsetCommand(self, ctx:RedisParser.LsetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#ltrimCommand.
    def enterLtrimCommand(self, ctx:RedisParser.LtrimCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#ltrimCommand.
    def exitLtrimCommand(self, ctx:RedisParser.LtrimCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#copyCommand.
    def enterCopyCommand(self, ctx:RedisParser.CopyCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#copyCommand.
    def exitCopyCommand(self, ctx:RedisParser.CopyCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#dbClause.
    def enterDbClause(self, ctx:RedisParser.DbClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#dbClause.
    def exitDbClause(self, ctx:RedisParser.DbClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#databaseName.
    def enterDatabaseName(self, ctx:RedisParser.DatabaseNameContext):
        pass

    # Exit a parse tree produced by RedisParser#databaseName.
    def exitDatabaseName(self, ctx:RedisParser.DatabaseNameContext):
        pass


    # Enter a parse tree produced by RedisParser#deleteCommand.
    def enterDeleteCommand(self, ctx:RedisParser.DeleteCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#deleteCommand.
    def exitDeleteCommand(self, ctx:RedisParser.DeleteCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#unlinkCommand.
    def enterUnlinkCommand(self, ctx:RedisParser.UnlinkCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#unlinkCommand.
    def exitUnlinkCommand(self, ctx:RedisParser.UnlinkCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#dumpCommand.
    def enterDumpCommand(self, ctx:RedisParser.DumpCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#dumpCommand.
    def exitDumpCommand(self, ctx:RedisParser.DumpCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#existsCommand.
    def enterExistsCommand(self, ctx:RedisParser.ExistsCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#existsCommand.
    def exitExistsCommand(self, ctx:RedisParser.ExistsCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#expireCommand.
    def enterExpireCommand(self, ctx:RedisParser.ExpireCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#expireCommand.
    def exitExpireCommand(self, ctx:RedisParser.ExpireCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#expireAtCommand.
    def enterExpireAtCommand(self, ctx:RedisParser.ExpireAtCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#expireAtCommand.
    def exitExpireAtCommand(self, ctx:RedisParser.ExpireAtCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#pExpireCommand.
    def enterPExpireCommand(self, ctx:RedisParser.PExpireCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#pExpireCommand.
    def exitPExpireCommand(self, ctx:RedisParser.PExpireCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#pExpireAtCommand.
    def enterPExpireAtCommand(self, ctx:RedisParser.PExpireAtCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#pExpireAtCommand.
    def exitPExpireAtCommand(self, ctx:RedisParser.PExpireAtCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#expireOptions.
    def enterExpireOptions(self, ctx:RedisParser.ExpireOptionsContext):
        pass

    # Exit a parse tree produced by RedisParser#expireOptions.
    def exitExpireOptions(self, ctx:RedisParser.ExpireOptionsContext):
        pass


    # Enter a parse tree produced by RedisParser#expireTimeCommand.
    def enterExpireTimeCommand(self, ctx:RedisParser.ExpireTimeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#expireTimeCommand.
    def exitExpireTimeCommand(self, ctx:RedisParser.ExpireTimeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#pExpireTimeCommand.
    def enterPExpireTimeCommand(self, ctx:RedisParser.PExpireTimeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#pExpireTimeCommand.
    def exitPExpireTimeCommand(self, ctx:RedisParser.PExpireTimeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#keysCommand.
    def enterKeysCommand(self, ctx:RedisParser.KeysCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#keysCommand.
    def exitKeysCommand(self, ctx:RedisParser.KeysCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#moveCommand.
    def enterMoveCommand(self, ctx:RedisParser.MoveCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#moveCommand.
    def exitMoveCommand(self, ctx:RedisParser.MoveCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#objectCommand.
    def enterObjectCommand(self, ctx:RedisParser.ObjectCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#objectCommand.
    def exitObjectCommand(self, ctx:RedisParser.ObjectCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#objectOptions.
    def enterObjectOptions(self, ctx:RedisParser.ObjectOptionsContext):
        pass

    # Exit a parse tree produced by RedisParser#objectOptions.
    def exitObjectOptions(self, ctx:RedisParser.ObjectOptionsContext):
        pass


    # Enter a parse tree produced by RedisParser#persistCommand.
    def enterPersistCommand(self, ctx:RedisParser.PersistCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#persistCommand.
    def exitPersistCommand(self, ctx:RedisParser.PersistCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#ttlCommand.
    def enterTtlCommand(self, ctx:RedisParser.TtlCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#ttlCommand.
    def exitTtlCommand(self, ctx:RedisParser.TtlCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#pTtlCommand.
    def enterPTtlCommand(self, ctx:RedisParser.PTtlCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#pTtlCommand.
    def exitPTtlCommand(self, ctx:RedisParser.PTtlCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#randomKeyCommand.
    def enterRandomKeyCommand(self, ctx:RedisParser.RandomKeyCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#randomKeyCommand.
    def exitRandomKeyCommand(self, ctx:RedisParser.RandomKeyCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#renameCommand.
    def enterRenameCommand(self, ctx:RedisParser.RenameCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#renameCommand.
    def exitRenameCommand(self, ctx:RedisParser.RenameCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#renameNxCommand.
    def enterRenameNxCommand(self, ctx:RedisParser.RenameNxCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#renameNxCommand.
    def exitRenameNxCommand(self, ctx:RedisParser.RenameNxCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#scanCommand.
    def enterScanCommand(self, ctx:RedisParser.ScanCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#scanCommand.
    def exitScanCommand(self, ctx:RedisParser.ScanCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#matchClause.
    def enterMatchClause(self, ctx:RedisParser.MatchClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#matchClause.
    def exitMatchClause(self, ctx:RedisParser.MatchClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#countClause.
    def enterCountClause(self, ctx:RedisParser.CountClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#countClause.
    def exitCountClause(self, ctx:RedisParser.CountClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#typeClause.
    def enterTypeClause(self, ctx:RedisParser.TypeClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#typeClause.
    def exitTypeClause(self, ctx:RedisParser.TypeClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#touchCommand.
    def enterTouchCommand(self, ctx:RedisParser.TouchCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#touchCommand.
    def exitTouchCommand(self, ctx:RedisParser.TouchCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#typeCommand.
    def enterTypeCommand(self, ctx:RedisParser.TypeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#typeCommand.
    def exitTypeCommand(self, ctx:RedisParser.TypeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#waitCommand.
    def enterWaitCommand(self, ctx:RedisParser.WaitCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#waitCommand.
    def exitWaitCommand(self, ctx:RedisParser.WaitCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#stringSetCommand.
    def enterStringSetCommand(self, ctx:RedisParser.StringSetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#stringSetCommand.
    def exitStringSetCommand(self, ctx:RedisParser.StringSetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#keyExistenceClause.
    def enterKeyExistenceClause(self, ctx:RedisParser.KeyExistenceClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#keyExistenceClause.
    def exitKeyExistenceClause(self, ctx:RedisParser.KeyExistenceClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#expirationClause.
    def enterExpirationClause(self, ctx:RedisParser.ExpirationClauseContext):
        pass

    # Exit a parse tree produced by RedisParser#expirationClause.
    def exitExpirationClause(self, ctx:RedisParser.ExpirationClauseContext):
        pass


    # Enter a parse tree produced by RedisParser#getCommand.
    def enterGetCommand(self, ctx:RedisParser.GetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#getCommand.
    def exitGetCommand(self, ctx:RedisParser.GetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#incrementCommand.
    def enterIncrementCommand(self, ctx:RedisParser.IncrementCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#incrementCommand.
    def exitIncrementCommand(self, ctx:RedisParser.IncrementCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#incrementByCommand.
    def enterIncrementByCommand(self, ctx:RedisParser.IncrementByCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#incrementByCommand.
    def exitIncrementByCommand(self, ctx:RedisParser.IncrementByCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#decrementCommand.
    def enterDecrementCommand(self, ctx:RedisParser.DecrementCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#decrementCommand.
    def exitDecrementCommand(self, ctx:RedisParser.DecrementCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#decrementByCommand.
    def enterDecrementByCommand(self, ctx:RedisParser.DecrementByCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#decrementByCommand.
    def exitDecrementByCommand(self, ctx:RedisParser.DecrementByCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#appendCommand.
    def enterAppendCommand(self, ctx:RedisParser.AppendCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#appendCommand.
    def exitAppendCommand(self, ctx:RedisParser.AppendCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#getDeleteCommand.
    def enterGetDeleteCommand(self, ctx:RedisParser.GetDeleteCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#getDeleteCommand.
    def exitGetDeleteCommand(self, ctx:RedisParser.GetDeleteCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#getExCommand.
    def enterGetExCommand(self, ctx:RedisParser.GetExCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#getExCommand.
    def exitGetExCommand(self, ctx:RedisParser.GetExCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#getRangeCommand.
    def enterGetRangeCommand(self, ctx:RedisParser.GetRangeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#getRangeCommand.
    def exitGetRangeCommand(self, ctx:RedisParser.GetRangeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#getSetCommand.
    def enterGetSetCommand(self, ctx:RedisParser.GetSetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#getSetCommand.
    def exitGetSetCommand(self, ctx:RedisParser.GetSetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#mGetCommand.
    def enterMGetCommand(self, ctx:RedisParser.MGetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#mGetCommand.
    def exitMGetCommand(self, ctx:RedisParser.MGetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#mSetCommand.
    def enterMSetCommand(self, ctx:RedisParser.MSetCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#mSetCommand.
    def exitMSetCommand(self, ctx:RedisParser.MSetCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#mSetNxCommand.
    def enterMSetNxCommand(self, ctx:RedisParser.MSetNxCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#mSetNxCommand.
    def exitMSetNxCommand(self, ctx:RedisParser.MSetNxCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#pSetExCommand.
    def enterPSetExCommand(self, ctx:RedisParser.PSetExCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#pSetExCommand.
    def exitPSetExCommand(self, ctx:RedisParser.PSetExCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#setExCommand.
    def enterSetExCommand(self, ctx:RedisParser.SetExCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#setExCommand.
    def exitSetExCommand(self, ctx:RedisParser.SetExCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#setNxCommand.
    def enterSetNxCommand(self, ctx:RedisParser.SetNxCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#setNxCommand.
    def exitSetNxCommand(self, ctx:RedisParser.SetNxCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#setRangeCommand.
    def enterSetRangeCommand(self, ctx:RedisParser.SetRangeCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#setRangeCommand.
    def exitSetRangeCommand(self, ctx:RedisParser.SetRangeCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#stringLengthCommand.
    def enterStringLengthCommand(self, ctx:RedisParser.StringLengthCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#stringLengthCommand.
    def exitStringLengthCommand(self, ctx:RedisParser.StringLengthCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#substringCommand.
    def enterSubstringCommand(self, ctx:RedisParser.SubstringCommandContext):
        pass

    # Exit a parse tree produced by RedisParser#substringCommand.
    def exitSubstringCommand(self, ctx:RedisParser.SubstringCommandContext):
        pass


    # Enter a parse tree produced by RedisParser#decimal.
    def enterDecimal(self, ctx:RedisParser.DecimalContext):
        pass

    # Exit a parse tree produced by RedisParser#decimal.
    def exitDecimal(self, ctx:RedisParser.DecimalContext):
        pass


    # Enter a parse tree produced by RedisParser#decimalScore.
    def enterDecimalScore(self, ctx:RedisParser.DecimalScoreContext):
        pass

    # Exit a parse tree produced by RedisParser#decimalScore.
    def exitDecimalScore(self, ctx:RedisParser.DecimalScoreContext):
        pass


    # Enter a parse tree produced by RedisParser#identifier.
    def enterIdentifier(self, ctx:RedisParser.IdentifierContext):
        pass

    # Exit a parse tree produced by RedisParser#identifier.
    def exitIdentifier(self, ctx:RedisParser.IdentifierContext):
        pass


    # Enter a parse tree produced by RedisParser#lexicalScore.
    def enterLexicalScore(self, ctx:RedisParser.LexicalScoreContext):
        pass

    # Exit a parse tree produced by RedisParser#lexicalScore.
    def exitLexicalScore(self, ctx:RedisParser.LexicalScoreContext):
        pass


    # Enter a parse tree produced by RedisParser#stringKeyName.
    def enterStringKeyName(self, ctx:RedisParser.StringKeyNameContext):
        pass

    # Exit a parse tree produced by RedisParser#stringKeyName.
    def exitStringKeyName(self, ctx:RedisParser.StringKeyNameContext):
        pass


    # Enter a parse tree produced by RedisParser#listKeyName.
    def enterListKeyName(self, ctx:RedisParser.ListKeyNameContext):
        pass

    # Exit a parse tree produced by RedisParser#listKeyName.
    def exitListKeyName(self, ctx:RedisParser.ListKeyNameContext):
        pass


    # Enter a parse tree produced by RedisParser#setKeyName.
    def enterSetKeyName(self, ctx:RedisParser.SetKeyNameContext):
        pass

    # Exit a parse tree produced by RedisParser#setKeyName.
    def exitSetKeyName(self, ctx:RedisParser.SetKeyNameContext):
        pass


    # Enter a parse tree produced by RedisParser#sortedSetKeyName.
    def enterSortedSetKeyName(self, ctx:RedisParser.SortedSetKeyNameContext):
        pass

    # Exit a parse tree produced by RedisParser#sortedSetKeyName.
    def exitSortedSetKeyName(self, ctx:RedisParser.SortedSetKeyNameContext):
        pass


    # Enter a parse tree produced by RedisParser#hashKeyName.
    def enterHashKeyName(self, ctx:RedisParser.HashKeyNameContext):
        pass

    # Exit a parse tree produced by RedisParser#hashKeyName.
    def exitHashKeyName(self, ctx:RedisParser.HashKeyNameContext):
        pass


    # Enter a parse tree produced by RedisParser#keyName.
    def enterKeyName(self, ctx:RedisParser.KeyNameContext):
        pass

    # Exit a parse tree produced by RedisParser#keyName.
    def exitKeyName(self, ctx:RedisParser.KeyNameContext):
        pass


    # Enter a parse tree produced by RedisParser#notProperPattern.
    def enterNotProperPattern(self, ctx:RedisParser.NotProperPatternContext):
        pass

    # Exit a parse tree produced by RedisParser#notProperPattern.
    def exitNotProperPattern(self, ctx:RedisParser.NotProperPatternContext):
        pass



del RedisParser