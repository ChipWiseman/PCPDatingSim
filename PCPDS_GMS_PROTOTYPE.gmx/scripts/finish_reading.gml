///finish_reading()
if(PlayerController.enter)
{    
    io_clear();
    if(!skip)
    {
        NPCText.spd = 100;
        skip=true;
    }
    else
    {
        instance_destroy(NPCText);
        skip=false;
        DiaIndex++;
        done = true;
    }
}
