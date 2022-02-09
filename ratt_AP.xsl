<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body style="display:flex;justify-content:center;align-items:center;flex-direction:column;font-family:system-ui!important;">
        <h2>Note</h2>
        <table border="0" style="flex-grow:1;flex-shrink:1;width:80%">
          <tr bgcolor="7fe1f1" style="min-width:250px;height:50px;display:flex;justify-content:center;align-items:center">
            <th style="text-align:left">cne</th>
            <xsl:for-each select="note/student[1]/module">
              <th>
                <xsl:value-of select="name"/>
              </th>
            </xsl:for-each>
          </tr>
          <xsl:for-each select="note/student">
            <tr bgcolor="7fe1f1" style="min-width:250px;height:50px;display:flex;justify-content:center;align-items:center">
              <td style="display:flex;justify-content:center;align-items:center">
                <xsl:value-of select="cne"/>
              </td>
              <xsl:for-each select="module">
                <xsl:variable name="value" select="note"/>
                  <xsl:if test="$value &gt;= 10"> 
                    <td style="background:#aaf17f;display:flex;justify-content:center;align-items:center">
                      <span stye="font-size:30px;">
                        <xsl:text>V</xsl:text>
                      </span>
                    </td>
                  </xsl:if>        
                  <xsl:if test="$value &gt;= 7 and $value &lt; 10"> 
                    <td style="background:#f1bb7f;display:flex;justify-content:center;align-items:center">
                      <span stye="font-size:30px;">
                        <xsl:text>NV</xsl:text>
                      </span>
                    </td>
                  </xsl:if> 
                  <xsl:if test="$value &gt;= 0 and $value &lt; 7"> 
                    <td style="background:#f17f7f;display:flex;justify-content:center;align-items:center">
                      <span stye="font-size:30px;">
                        <xsl:text>NV</xsl:text>
                      </span>
                    </td>
                  </xsl:if>         
              </xsl:for-each>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>