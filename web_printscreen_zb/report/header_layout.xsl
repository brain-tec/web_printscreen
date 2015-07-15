<?xml version = '1.0' encoding="utf-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <xsl:template name="first_page_graphics_corporation">

        <fill color="black"/>
        <stroke color="black"/>
        <setFont name="DejaVu Sans Bold" size="10"/>

        <drawString x="13.8cm" y="18.8cm"><xsl:value-of select="//company"/></drawString>

        <stroke color="#000000"/>
        <lines size="8">1.3cm 18.6cm 28.5cm 18.6cm</lines>
        <lines size="8">1.3cm 2cm 28.5cm 2cm</lines>

        <stroke color="black"/>
        <setFont name="Helvetica" size="10"/>
        <drawString x="1.3cm" y="1.5cm"><xsl:value-of select="//header-date"/></drawString>

        <place x="1.3cm" y="0cm" height="2.55cm" width="19.0cm">
            <para style="main_footer"><pageNumber/></para>
        </place>

    </xsl:template>

   <xsl:template name="first_page_frames">
            <frame id="col1" x1="2.0cm" y1="2.5cm" width="24.7cm" height="16cm"/>
    </xsl:template>

</xsl:stylesheet>
