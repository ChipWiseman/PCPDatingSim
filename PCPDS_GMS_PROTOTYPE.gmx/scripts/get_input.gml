///get_input()
up = max(keyboard_check(vk_up),keyboard_check(ord('W')),0);
left = max(keyboard_check(vk_left),keyboard_check(ord('A')),0);
down = max(keyboard_check(vk_down),keyboard_check(ord('S')),0);
right = max(keyboard_check(vk_right),keyboard_check(ord('D')),0);

space = keyboard_check(vk_space);
space_release = keyboard_check_released(vk_space);
esc = keyboard_check_released(vk_escape);
tab = keyboard_check_released(vk_tab);
enter = keyboard_check_released(vk_enter);
