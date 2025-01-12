PDF_FILE_TEMPLATE = """
%PDF-1.6

% Root
1 0 obj
<<
  /AcroForm <<
    /Fields [ ###FIELD_LIST### ]
  >>
  /Pages <<
    /Count 1
    /Kids [ 4
      16 0 R
    ]
    /Type /Pages
  >>
  /OpenAction 17 0 R
  /Type /Catalog
>>
endobj

%% Annots Page 1 (also used as overall fields list)
21 0 obj
[
  ###FIELD_LIST###
]
endobj

###FIELDS###

%% Page 1
16 0 obj
<<
  /Annots 21 0 R
  /Contents << >>
  /CropBox [
    0.0
    0.0
    612.0
    792.0
  ]
  /MediaBox [
    0.0
    0.0
    612.0
    792.0
  ]
  /Parent 7 0 R
  /Resources <<
  >>
  /Rotate 0
  /Type /Page
>>
endobj

17 0 obj
<<
  /JS 42 0 R
  /S /JavaScript
>>
endobj

42 0 obj
<< >>
stream

function setInterval(cb, ms) {
    evalStr = "(" + cb.toString() + ")();";
    return app.setInterval(evalStr, ms);
}

function updateStyle(element, bgColor, borderRadius, fontSize) {
    element.strokeColor = color.gray;
    element.fillColor = bgColor;
    element.borderRadius = borderRadius;
    element.textSize = fontSize;
}

function initializeUI() {
    var leftButton = this.getField("B_left");
    updateStyle(leftButton, color.blue, 5, 14);

    var rightButton = this.getField("B_right");
    updateStyle(rightButton, color.blue, 5, 14);

    var downButton = this.getField("B_down");
    updateStyle(downButton, color.green, 5, 14);

    var rotateButton = this.getField("B_rotate");
    updateStyle(rotateButton, color.red, 5, 14);

    var startButton = this.getField("B_start");
    updateStyle(startButton, color.orange, 10, 16);

    var scoreField = this.getField("T_score");
    scoreField.textColor = color.black;
    scoreField.textSize = 18;
    scoreField.alignment = "center";
}

initializeUI();
endstream
endobj

18 0 obj
<<
  /JS 43 0 R
  /S /JavaScript
>>
endobj

43 0 obj
<< >>
stream
initializeUI();
endstream
endobj

trailer
<<
  /Root 1 0 R
>>

%%EOF
"""

PX_SIZE = 20
GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_OFF_X = 200
GRID_OFF_Y = 350

# Playing field grid lines and colored cells
pixel_fields = """###FIELDS###"""

filled_pdf = PDF_FILE_TEMPLATE.replace("###FIELDS###", pixel_fields)
filled_pdf = filled_pdf.replace("###FIELD_LIST###", " ")

with open("cool_pdf_tetris.pdf", "w") as pdffile:
    pdffile.write(filled_pdf)

print("enhanced UI")
