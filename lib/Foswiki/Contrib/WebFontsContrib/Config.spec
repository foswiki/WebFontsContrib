# ---+ Extensions
# ---++ JQueryPlugin
# ---+++ General settings 
# **PERL H EXPERT**
$Foswiki::cfg{JQueryPlugin}{IconFonts}{material} = {
  'prefix' => 'ma',
  'definition' => '$Foswiki::cfg{PubDir}/$Foswiki::cfg{SystemWebName}/WebFontsContrib/material-icons/material.json',
  'css' => '$Foswiki::cfg{PubUrlPath}/$Foswiki::cfg{SystemWebName}/WebFontsContrib/material-icons/font-face.css', 
};
# **PERL H EXPERT**
# WARNING: tabler-icon font slows down page loading time under MS Windows
$Foswiki::cfg{JQueryPlugin}{IconFonts}{tabler} = {
  'prefix' => 'ti',
  'definition' => '$Foswiki::cfg{PubDir}/$Foswiki::cfg{SystemWebName}/WebFontsContrib/tabler-icons/tabler-icons.json',
  'css' => '$Foswiki::cfg{PubUrlPath}/$Foswiki::cfg{SystemWebName}/WebFontsContrib/tabler-icons/font-face.css', 
};

1;
