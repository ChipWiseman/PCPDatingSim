///keep_reading_dialogue(int)
int = argument0;
if(PlayerController.enter)
{    
    io_clear();
    if(skip==0)
    {
        NPCText.spd = 100;
        skip=1;
    }
    else if(int == 0)
    {
        instance_destroy(NPCText);
        DiaIndex++;
        skip=0;
    }
    else if(int>0)
    {
        instance_destroy(NPCText);
        DiaIndex = int;
        skip=0;
    }
}
