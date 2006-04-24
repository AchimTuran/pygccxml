# Copyright 2004 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

"""
defines class, that describes C++ namespace
"""
import declaration
import scopedef
import algorithm

class namespace_t( scopedef.scopedef_t ):
    """
    describes C++ namespace
    """
    
    def __init__( self, name='', parent=None, declarations=None ):
        scopedef.scopedef_t.__init__( self, name, parent )
        if not declarations:
            declarations = []
        self._declarations = declarations # list of all declarations belongs to this namespace

    def __str__(self):
        name = algorithm.full_name(self)
        if name!="::" and name[:2]=="::":
            name = name[2:]
        return "%s [namespace]"%name

    def _get__cmp__scope_items(self):
        return [ self._sorted_list( self.declarations ) ]
        
    def _get_declarations_impl(self):
        return self._declarations
    def _set_declarations(self, declarations):
        self._declarations = declarations
    declarations = property( scopedef.scopedef_t._get_declarations, _set_declarations )
        
    def take_parenting( self, inst ):
        """Takes parenting from inst and transfers it to self"""
        if self is inst:
            return
        for decl in inst.declarations:
            decl.parent = self
            self.declarations.append( decl )
        inst.declarations = []
        
    def remove_declaration( self, decl ):
        """
        removes decl from  members list
        
        @param decl: declaration to be removed
        @type decl: L{declaration_t}
        """
        del self.declarations[ self.declarations.index( decl ) ]
        #add more comment about this.
        #if not keep_parent:
        #    decl.parent=None

    def namespace( self, name=None, function=None, recursive=None ):
        return self._find_single( scopedef.scopedef_t._impl_matchers[ namespace_t.namespace ]
                                  , name=name
                                  , function=function
                                  , recursive=recursive )

    def namespaces( self, name=None, function=None, recursive=None ):
        return self._find_multiple( scopedef.scopedef_t._impl_matchers[ namespace_t.namespace ]
                                    , name=name
                                    , function=function
                                    , recursive=recursive )

    def free_function( self, name=None, function=None, return_type=None, arg_types=None, header_dir=None, header_file=None, recursive=None ):
        return self._find_single( scopedef.scopedef_t._impl_matchers[ namespace_t.free_function ]
                                  , name=name
                                  , function=function
                                  , decl_type=self._impl_decl_types[ namespace_t.free_function ]
                                  , return_type=return_type
                                  , arg_types=arg_types 
                                  , header_dir=header_dir
                                  , header_file=header_file 
                                  , recursive=recursive )

    def free_functions( self, name=None, function=None, return_type=None, arg_types=None, header_dir=None, header_file=None, recursive=None ):
        return self._find_multiple( scopedef.scopedef_t._impl_matchers[ namespace_t.free_function ]
                                    , name=name
                                    , function=function
                                    , decl_type=self._impl_decl_types[ namespace_t.free_function ]
                                    , return_type=return_type
                                    , arg_types=arg_types 
                                    , header_dir=header_dir
                                    , header_file=header_file
                                    , recursive=recursive)

    def free_operator( self, name=None, function=None, symbol=None, return_type=None, arg_types=None, header_dir=None, header_file=None, recursive=None ):
        return self._find_single( scopedef.scopedef_t._impl_matchers[ namespace_t.free_operator ]
                                  , name=name
                                  , symbol=symbol
                                  , function=function
                                  , decl_type=self._impl_decl_types[ namespace_t.free_operator ]
                                  , return_type=return_type
                                  , arg_types=arg_types 
                                  , header_dir=header_dir
                                  , header_file=header_file 
                                  , recursive=recursive )

    def free_operators( self, name=None, function=None, symbol=None, return_type=None, arg_types=None, header_dir=None, header_file=None, recursive=None ):
        return self._find_multiple( scopedef.scopedef_t._impl_matchers[ namespace_t.free_operator ]
                                    , name=name
                                    , symbol=symbol
                                    , function=function
                                    , decl_type=self._impl_decl_types[ namespace_t.free_operator ]
                                    , return_type=return_type
                                    , arg_types=arg_types 
                                    , header_dir=header_dir
                                    , header_file=header_file 
                                    , recursive=recursive )