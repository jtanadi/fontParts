class BaseFont(BaseObject):

    def __repr__(self):
        pass

    def __eq__(self):
        """
        XXX

        How should this be implemented?
        Path comparison? Data comparison?
        Maybe we should just remove it.

        XXX
        """

    def __len__(self):
        """
        The number of glyphs in the default layer.
        """

    # ----------
    # Properties
    # ----------

    def _get_path(self):
        self.raiseNotImplemented()

    def _set_path(self, value):
        self.raiseNotImplemented()

    path = property(_get_path, _set_path, "The path to the file this object represents.")

    def _get_info(self):
        self.raiseNotImplemented()

    def _set_info(self, value):
        self.raiseNotImplemented()

    info = property(_get_info, _set_info, "The font's info object.")

    def _get_groups(self):
        self.raiseNotImplemented()

    def _set_groups(self, value):
        self.raiseNotImplemented()

    groups = property(_get_groups, _set_groups, "The font's groups object.")

    def _get_kerning(self):
        self.raiseNotImplemented()

    def _set_kerning(self, value):
        self.raiseNotImplemented()

    kerning = property(_get_kerning, _set_kerning, "The font's kerning object.")

    def _get_features(self):
        self.raiseNotImplemented()

    def _set_features(self, value):
        self.raiseNotImplemented()

    features = property(_get_features, _set_features, "The font's features object.")

    def _get_lib(self):
        self.raiseNotImplemented()

    def _set_lib(self, value):
        self.raiseNotImplemented()

    lib = property(_get_lib, _set_lib, "The font's lib object.")

    # ---------------
    # File Operations
    # ---------------

    def open(self, path, showInterface=True):
        """
        Open the file located at path. The type of files
        that can be opened will be defined by the environment.

        showInterface indicates if the user interface
        should be opened or not. Environments may or may not
        implement this behavior.
        """
        self.raiseNotImplementedError()

    def save(self, path=None, showProgress=False, formatVersion=None):
        """
        Save the font to path. If path is None, use the font's
        original location. The file type must be inferred from
        the file extension on the given path. If no file extension
        is given, the environment may fall back to the format
        of its choice.

        showProgress indicates if a progress indicator should be
        displayed during the operation. Environments may or may not
        implement this behavior.

        formatVersion indicates the format version that should
        be used for writing the given file type. For example, if
        2 is given for formatVersion and the file type being written
        if UFO, the file is to be written in UFO 2 format. This
        value is not limited to UFO format versions. If no
        format version is given, the original format version of
        the file should be preserved. If there is no original
        format version it is implied that the format version
        is the latest version for the file type as supported
        by the environment.

        Environments may define their own rules governing when
        a file should be saved into its original location and
        when it should not. For example, a font opened from a
        compiled OpenType font may not be written back into
        the original OpenType font.
        """
        self.raiseNotImplementedError()

    def close(self, save=False):
        """
        Close the font. If save is True, call the save method
        is called with no arguments.
        """
        self.raiseNotImplementedError()

    def generate(self, format, path=None):
        """
        Generate the font to another format.

        format defines the file format to output. These are the standard

        mactype1     = Mac Type 1 font (generates suitcase  and LWFN file)
        macttf       = Mac TrueType font (generates suitcase)
        macttdfont   = Mac TrueType font (generates suitcase with resources in data fork)
        otfcff       = PS OpenType (CFF-based) font (OTF)
        otfttf       = PC TrueType/TT OpenType font (TTF)
        pctype1      = PC Type 1 font (binary/PFB)
        pcmm         = PC MultipleMaster font (PFB)
        pctype1ascii = PC Type 1 font (ASCII/PFA)
        pcmmascii    = PC MultipleMaster font (ASCII/PFA)
        ufo1         = UFO format version 1
        ufo2         = UFO format version 2
        ufo3         = UFO format version 3
        unixascii    = UNIX ASCII font (ASCII/PFA)

        Environments are not required to support all of these.
        Environments may define their own format types.

        path defines the location where the new file should
        be located. If path defines a directory, the file should
        be output as the current file name, with the appropriate
        suffix for the format, into the given directory. If no path
        is given, the file will be output into the same directory
        as the source font with the file named with the current
        file name, with the appropriate suffix for the format.
        """
        self.raiseNotImplementedError()

    # -----------------------
    # Global Glyph Operations
    # -----------------------

    def round(self):
        """
        Round all approriate data to integers. This is the
        equivalent of calling the round method on each object
        within the font.

        This applies only to the default layer.
        """

    def autoUnicodes(self):
        """
        Assign Unicode values to all glyphs in the font.
        Environments will define their own algorithms for
        automatically assigning values.

        This applies only to the default layer.
        """

    # ------------------
    # Reference Mappings
    # ------------------

    def getCharacterMapping(self):
        """
        Get a dictionary showing unicode to glyph mapping.

            {
                unicode value : [glyph names]
            }

        This applies only to the default layer.
        """

    def getReverseComponentMapping(self):
        """
        Get a dictionary showing component references.

            {
                base glyph name : [glyph names]
            }

        This applies only to the default layer.
        """

    # -----------------
    # Glyph Interaction
    # -----------------

    def __iter__(self):
        """
        Iterate through the glyphs in the default layer.
        """

    def __getitem__(self, name):
        """
        Get the glyph with name from the default layer.
        """

    def keys(self):
        """
        Get a list of all glyphs in the default layer
        of the font. The order of the glyphs is undefined.
        """

    def __contains__(self, name):
        """
        Test if the default layer contains a glyph with name.
        """

    has_key = __contains__

    def newGlyph(self, name, clear=True):
        """
        Make a new glyph in the default layer. The
        glyph will be returned.

        clear indicates if the data in an existing glyph
        with the same name should be cleared. If so,
        the clear method of the glyph should be called.
        """

    def removeGlyph(self, name):
        """
        Remove the glyph with name from the default layer.
        """

    def insertGlyph(self, glyph, name=None):
        """
        Insert a new glyph into the default layer.
        The glyph will be returned.

        name indicates the name that should be assigned to
        the glyph after insertion. If name is not given,
        the glyph's original name must be used. If the glyph
        does not have a name, an error must be raised.

        This does not insert the given glyph object. Instead,
        a new glyph is created and the data from the given
        glyph is recreated in the new glyph.
        """

    # -------------
    # Interpolation
    # -------------

    def interpolate(self, factor, minFont, maxFont, suppressError=True, analyzeOnly=False, showProgress=False):
        """
        Interpolate all possible data in the font. The interpolation
        occurs on a 0 to 1.0 range where minFont is located at
        0 and maxFont is located at 1.0.

        factor is the interpolation value. It may be less than 0
        and greater than 1.0. It may be a number (integer, float)
        or a tuple of two numbers. If it is a tuple, the first
        number indicates the x factor and the second number
        indicates the y factor.

        suppressError indicates if incompatible data should be ignored
        or if an error should be raised when such incompatibilities are found.

        analyzeOnly indicates if the intrpolation should only be a
        compatibiltiy check with no interpolation actually performed.
        If this is True, a dict of compatibility problems will
        be returned.
        """
