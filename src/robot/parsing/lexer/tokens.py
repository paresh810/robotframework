#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from robot.utils import py2to3


@py2to3
class Token(object):
    SETTING_HEADER = 'SETTING_HEADER'
    VARIABLE_HEADER = 'VARIABLE_HEADER'
    TESTCASE_HEADER = 'TESTCASE_HEADER'
    KEYWORD_HEADER = 'KEYWORD_HEADER'
    COMMENT_HEADER = 'COMMENT_HEADER'

    DOCUMENTATION = 'DOCUMENTATION'
    SUITE_SETUP = 'SUITE_SETUP'
    SUITE_TEARDOWN = 'SUITE_TEARDOWN'
    METADATA = 'METADATA'
    TEST_SETUP = 'TEST_SETUP'
    TEST_TEARDOWN = 'TEST_TEARDOWN'
    TEST_TEMPLATE = 'TEST_TEMPLATE'
    TEST_TIMEOUT = 'TEST_TIMEOUT'
    FORCE_TAGS = 'FORCE_TAGS'
    DEFAULT_TAGS = 'DEFAULT_TAGS'
    LIBRARY = 'LIBRARY'
    RESOURCE = 'RESOURCE'
    VARIABLES = 'VARIABLES'
    SETUP = 'SETUP'
    TEARDOWN = 'TEARDOWN'
    TEMPLATE = 'TEMPLATE'
    TIMEOUT = 'TIMEOUT'
    TAGS = 'TAGS'
    ARGUMENTS = 'ARGUMENTS'
    RETURN = 'RETURN'

    VARIABLE = 'VARIABLE'
    ARGUMENT = 'ARGUMENT'
    NAME = 'NAME'
    ASSIGN = 'ASSIGN'
    KEYWORD = 'KEYWORD'
    FOR = 'FOR'
    FOR_SEPARATOR = 'FOR_SEPARATOR'
    OLD_FOR_INDENT = 'OLD_FOR_INDENT'
    END = 'END'

    SEPARATOR = 'SEPARATOR'
    EOL = 'EOL'
    COMMENT = 'COMMENT'
    CONTINUATION = 'CONTINUATION'
    IGNORE = 'IGNORE'
    EOS = 'EOS'
    ERROR = 'ERROR'
    DATA = 'DATA'

    NON_DATA_TOKENS = (
        SEPARATOR,
        COMMENT,
        CONTINUATION,
        IGNORE,
        EOL,
        EOS
    )
    SETTING_TOKENS = (
        DOCUMENTATION,
        SUITE_SETUP,
        SUITE_TEARDOWN,
        METADATA,
        TEST_SETUP,
        TEST_TEARDOWN,
        TEST_TEMPLATE,
        TEST_TIMEOUT,
        FORCE_TAGS,
        DEFAULT_TAGS,
        LIBRARY,
        RESOURCE,
        VARIABLES,
        SETUP,
        TEARDOWN,
        TEMPLATE,
        TIMEOUT,
        TAGS,
        ARGUMENTS,
        RETURN
    )
    HEADER_TOKENS = (
        SETTING_HEADER,
        VARIABLE_HEADER,
        TESTCASE_HEADER,
        KEYWORD_HEADER
    )

    __slots__ = ['type', 'value', 'lineno', 'columnno', 'error']

    def __init__(self, type, value='', lineno=-1, columnno=-1):
        self.type = type
        self.value = value
        self.lineno = lineno
        self.columnno = columnno
        self.error = None

    def __unicode__(self):
        return self.value

    def __repr__(self):
        return 'Token(%s, %r, %s, %s)' % (self.type, self.value,
                                          self.lineno, self.columnno)


class EOL(Token):
    __slots__ = []

    def __init__(self, value='', lineno=-1, columnno=-1):
        Token.__init__(self, Token.EOL, value, lineno, columnno)

    @classmethod
    def from_token(cls, token):
        return EOL('', token.lineno, token.columnno + len(token.value))


class EOS(Token):
    __slots__ = []

    def __init__(self, lineno=-1, columnno=-1):
        Token.__init__(self, Token.EOS, '', lineno, columnno)

    @classmethod
    def from_token(cls, token):
        return EOS(token.lineno, token.columnno + len(token.value))
