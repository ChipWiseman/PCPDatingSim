///PC_text_box("Text");
txt = instance_create(0,3*window_get_height()/4,PCText);
txt.text = argument0;
txt.font = fnt_text;  
txt.font_size = font_get_size(txt.font);
txt.text_length = string_length(txt.text);
