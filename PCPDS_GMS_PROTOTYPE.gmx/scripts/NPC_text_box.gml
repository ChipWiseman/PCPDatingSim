///NPC_text_box("Text",speed,font,char)
txt = instance_create(view_xview,view_yview,NPCText);
txt.text = argument0;
txt.spd = argument1;
txt.font = argument2;
txt.char = argument3
txt.done = 0;
txt.font_size = font_get_size(txt.font);
txt.text_length = string_length(txt.text);

