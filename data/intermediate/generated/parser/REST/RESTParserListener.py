# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/REST/RESTParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .RESTParser import RESTParser
else:
    from RESTParser import RESTParser

# This class defines a complete listener for a parse tree produced by RESTParser.
class RESTParserListener(ParseTreeListener):

    # Enter a parse tree produced by RESTParser#start.
    def enterStart(self, ctx:RESTParser.StartContext):
        pass

    # Exit a parse tree produced by RESTParser#start.
    def exitStart(self, ctx:RESTParser.StartContext):
        pass


    # Enter a parse tree produced by RESTParser#bodyElements.
    def enterBodyElements(self, ctx:RESTParser.BodyElementsContext):
        pass

    # Exit a parse tree produced by RESTParser#bodyElements.
    def exitBodyElements(self, ctx:RESTParser.BodyElementsContext):
        pass


    # Enter a parse tree produced by RESTParser#bodyElement.
    def enterBodyElement(self, ctx:RESTParser.BodyElementContext):
        pass

    # Exit a parse tree produced by RESTParser#bodyElement.
    def exitBodyElement(self, ctx:RESTParser.BodyElementContext):
        pass


    # Enter a parse tree produced by RESTParser#sectionTitle.
    def enterSectionTitle(self, ctx:RESTParser.SectionTitleContext):
        pass

    # Exit a parse tree produced by RESTParser#sectionTitle.
    def exitSectionTitle(self, ctx:RESTParser.SectionTitleContext):
        pass


    # Enter a parse tree produced by RESTParser#titleText.
    def enterTitleText(self, ctx:RESTParser.TitleTextContext):
        pass

    # Exit a parse tree produced by RESTParser#titleText.
    def exitTitleText(self, ctx:RESTParser.TitleTextContext):
        pass


    # Enter a parse tree produced by RESTParser#paragraph.
    def enterParagraph(self, ctx:RESTParser.ParagraphContext):
        pass

    # Exit a parse tree produced by RESTParser#paragraph.
    def exitParagraph(self, ctx:RESTParser.ParagraphContext):
        pass


    # Enter a parse tree produced by RESTParser#labeledParagraph.
    def enterLabeledParagraph(self, ctx:RESTParser.LabeledParagraphContext):
        pass

    # Exit a parse tree produced by RESTParser#labeledParagraph.
    def exitLabeledParagraph(self, ctx:RESTParser.LabeledParagraphContext):
        pass


    # Enter a parse tree produced by RESTParser#label.
    def enterLabel(self, ctx:RESTParser.LabelContext):
        pass

    # Exit a parse tree produced by RESTParser#label.
    def exitLabel(self, ctx:RESTParser.LabelContext):
        pass


    # Enter a parse tree produced by RESTParser#paragraphElements.
    def enterParagraphElements(self, ctx:RESTParser.ParagraphElementsContext):
        pass

    # Exit a parse tree produced by RESTParser#paragraphElements.
    def exitParagraphElements(self, ctx:RESTParser.ParagraphElementsContext):
        pass


    # Enter a parse tree produced by RESTParser#firstParagraphElement.
    def enterFirstParagraphElement(self, ctx:RESTParser.FirstParagraphElementContext):
        pass

    # Exit a parse tree produced by RESTParser#firstParagraphElement.
    def exitFirstParagraphElement(self, ctx:RESTParser.FirstParagraphElementContext):
        pass


    # Enter a parse tree produced by RESTParser#paragraphElement.
    def enterParagraphElement(self, ctx:RESTParser.ParagraphElementContext):
        pass

    # Exit a parse tree produced by RESTParser#paragraphElement.
    def exitParagraphElement(self, ctx:RESTParser.ParagraphElementContext):
        pass


    # Enter a parse tree produced by RESTParser#internalReference.
    def enterInternalReference(self, ctx:RESTParser.InternalReferenceContext):
        pass

    # Exit a parse tree produced by RESTParser#internalReference.
    def exitInternalReference(self, ctx:RESTParser.InternalReferenceContext):
        pass


    # Enter a parse tree produced by RESTParser#internalReferenceNoSpace.
    def enterInternalReferenceNoSpace(self, ctx:RESTParser.InternalReferenceNoSpaceContext):
        pass

    # Exit a parse tree produced by RESTParser#internalReferenceNoSpace.
    def exitInternalReferenceNoSpace(self, ctx:RESTParser.InternalReferenceNoSpaceContext):
        pass


    # Enter a parse tree produced by RESTParser#enumeration.
    def enterEnumeration(self, ctx:RESTParser.EnumerationContext):
        pass

    # Exit a parse tree produced by RESTParser#enumeration.
    def exitEnumeration(self, ctx:RESTParser.EnumerationContext):
        pass


    # Enter a parse tree produced by RESTParser#enumerationItems.
    def enterEnumerationItems(self, ctx:RESTParser.EnumerationItemsContext):
        pass

    # Exit a parse tree produced by RESTParser#enumerationItems.
    def exitEnumerationItems(self, ctx:RESTParser.EnumerationItemsContext):
        pass


    # Enter a parse tree produced by RESTParser#enumerationItem.
    def enterEnumerationItem(self, ctx:RESTParser.EnumerationItemContext):
        pass

    # Exit a parse tree produced by RESTParser#enumerationItem.
    def exitEnumerationItem(self, ctx:RESTParser.EnumerationItemContext):
        pass


    # Enter a parse tree produced by RESTParser#paragraphChars.
    def enterParagraphChars(self, ctx:RESTParser.ParagraphCharsContext):
        pass

    # Exit a parse tree produced by RESTParser#paragraphChars.
    def exitParagraphChars(self, ctx:RESTParser.ParagraphCharsContext):
        pass


    # Enter a parse tree produced by RESTParser#paragraphCharsNoSpace.
    def enterParagraphCharsNoSpace(self, ctx:RESTParser.ParagraphCharsNoSpaceContext):
        pass

    # Exit a parse tree produced by RESTParser#paragraphCharsNoSpace.
    def exitParagraphCharsNoSpace(self, ctx:RESTParser.ParagraphCharsNoSpaceContext):
        pass


    # Enter a parse tree produced by RESTParser#paragraphChar.
    def enterParagraphChar(self, ctx:RESTParser.ParagraphCharContext):
        pass

    # Exit a parse tree produced by RESTParser#paragraphChar.
    def exitParagraphChar(self, ctx:RESTParser.ParagraphCharContext):
        pass


    # Enter a parse tree produced by RESTParser#paragraphCharNoSpace.
    def enterParagraphCharNoSpace(self, ctx:RESTParser.ParagraphCharNoSpaceContext):
        pass

    # Exit a parse tree produced by RESTParser#paragraphCharNoSpace.
    def exitParagraphCharNoSpace(self, ctx:RESTParser.ParagraphCharNoSpaceContext):
        pass


    # Enter a parse tree produced by RESTParser#presep.
    def enterPresep(self, ctx:RESTParser.PresepContext):
        pass

    # Exit a parse tree produced by RESTParser#presep.
    def exitPresep(self, ctx:RESTParser.PresepContext):
        pass


    # Enter a parse tree produced by RESTParser#postsep.
    def enterPostsep(self, ctx:RESTParser.PostsepContext):
        pass

    # Exit a parse tree produced by RESTParser#postsep.
    def exitPostsep(self, ctx:RESTParser.PostsepContext):
        pass


    # Enter a parse tree produced by RESTParser#id.
    def enterId(self, ctx:RESTParser.IdContext):
        pass

    # Exit a parse tree produced by RESTParser#id.
    def exitId(self, ctx:RESTParser.IdContext):
        pass


    # Enter a parse tree produced by RESTParser#number.
    def enterNumber(self, ctx:RESTParser.NumberContext):
        pass

    # Exit a parse tree produced by RESTParser#number.
    def exitNumber(self, ctx:RESTParser.NumberContext):
        pass


    # Enter a parse tree produced by RESTParser#digitNonZero.
    def enterDigitNonZero(self, ctx:RESTParser.DigitNonZeroContext):
        pass

    # Exit a parse tree produced by RESTParser#digitNonZero.
    def exitDigitNonZero(self, ctx:RESTParser.DigitNonZeroContext):
        pass


    # Enter a parse tree produced by RESTParser#digits.
    def enterDigits(self, ctx:RESTParser.DigitsContext):
        pass

    # Exit a parse tree produced by RESTParser#digits.
    def exitDigits(self, ctx:RESTParser.DigitsContext):
        pass


    # Enter a parse tree produced by RESTParser#digit.
    def enterDigit(self, ctx:RESTParser.DigitContext):
        pass

    # Exit a parse tree produced by RESTParser#digit.
    def exitDigit(self, ctx:RESTParser.DigitContext):
        pass


    # Enter a parse tree produced by RESTParser#nobrString.
    def enterNobrString(self, ctx:RESTParser.NobrStringContext):
        pass

    # Exit a parse tree produced by RESTParser#nobrString.
    def exitNobrString(self, ctx:RESTParser.NobrStringContext):
        pass


    # Enter a parse tree produced by RESTParser#nobrChar.
    def enterNobrChar(self, ctx:RESTParser.NobrCharContext):
        pass

    # Exit a parse tree produced by RESTParser#nobrChar.
    def exitNobrChar(self, ctx:RESTParser.NobrCharContext):
        pass


    # Enter a parse tree produced by RESTParser#titleFirstChar.
    def enterTitleFirstChar(self, ctx:RESTParser.TitleFirstCharContext):
        pass

    # Exit a parse tree produced by RESTParser#titleFirstChar.
    def exitTitleFirstChar(self, ctx:RESTParser.TitleFirstCharContext):
        pass


    # Enter a parse tree produced by RESTParser#underline.
    def enterUnderline(self, ctx:RESTParser.UnderlineContext):
        pass

    # Exit a parse tree produced by RESTParser#underline.
    def exitUnderline(self, ctx:RESTParser.UnderlineContext):
        pass


    # Enter a parse tree produced by RESTParser#eqs.
    def enterEqs(self, ctx:RESTParser.EqsContext):
        pass

    # Exit a parse tree produced by RESTParser#eqs.
    def exitEqs(self, ctx:RESTParser.EqsContext):
        pass


    # Enter a parse tree produced by RESTParser#dashes.
    def enterDashes(self, ctx:RESTParser.DashesContext):
        pass

    # Exit a parse tree produced by RESTParser#dashes.
    def exitDashes(self, ctx:RESTParser.DashesContext):
        pass



del RESTParser