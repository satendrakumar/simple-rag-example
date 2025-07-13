# simple-rag-example
A minimal Retrieval Augmented Generation (RAG) API to answer climate-related questions.

## Usage

The API exposes a single endpoint for question answering:

**POST** `/v1/api/rag`  
**Body:**

### Local setup:
```shell
git clone https://github.com/satendrakumar/simple-rag-example.git
cd simple-rag-example
uv sync
python main.py
```


### Rest API Request and response:
```shell
1. Request:
    curl --location 'http://localhost:8000/v1/api/rag' \
    --header 'accept: application/json' \
    --header 'Content-Type: application/json' \
    --data '{
      "question": "How much has global temperature increased since pre-industrial times?"
    }'

  Response:
    {
    "response": " As per IPCC (2023), human activities, principally through emissions of greenhouse gases, have unequivocally caused global warming, with global surface temperature reaching 1.1°C above 1850 -1900 in 2011 -2020. Global greenhouse gas emissions have continued to increase over 2010 -2019,  with  unequal  historical  and  ongoing  contributions  arising  from unsustainable energy use, land use and land-use change, lifestyles and patterns of consumption and production across regions, between and within countries, and between individuals ( high confidence ). Human-caused climate change is already affecting many weather and climate extremes in every region across the globe. This has led to widespread adverse impacts on food and water security, human health and on economies and society and related losses and damages 63 to  nature  and people ( high confidence ).  Vulnerable communities who have historically contributed the least to current climate change are disproportionately affected ( high confidence ).\n63\n\nIt is unequivocal that human  influence has  warmed  the atmosphere, ocean and land. Widespread and rapid changes in the atmosphere, ocean, cryosphere and biosphere have occurred (Table 2.1). The scale of recent changes across the climate system as a whole and the present state of many aspects of the climate system are unprecedented over many centuries to many thousands of years. It is very likely that GHG emissions were the main driver 74 of tropospheric warming  and extremely  likely that  human-caused  stratospheric  ozone depletion was the main driver of stratospheric cooling between 1979 and the mid-1990s. It is virtually certain that the global upper ocean (0-700m)  has  warmed  since  the  1970s  and extremely  likely that human  influence  is  the  main  driver.  Ocean  warming  accounted  for 91% of the heating in the climate system, with land warming, ice loss and  atmospheric  warming  accounting  for  about  5%,  3%  and  1%, respectively ( high confidence ). Global mean sea level increased by 0.20 [0.15 to 0.25] m between 1901 and 2018. The average rate of sea level rise was 1.3 [0.6 to"
}
2. Request:
    curl --location 'http://localhost:8000/v1/api/rag' \
    --header 'accept: application/json' \
    --header 'Content-Type: application/json' \
    --data '{
      "question": "Is sea level rise avoidable? When will it stop?"
    }'
    Reponse: 
    {
    "response": "In the IPCC 2023 Synthesis Report, WGII SPM B.3.1 states:\n\nSea level rise is unavoidable for centuries to millennia due to continuing deep ocean warming and ice sheet melt, and sea levels will remain elevated for thousands of years (high-conﬁdence). Global mean sea level rise will continue in the 21st century (virtually certain), with projected regional relative sea level rise within 20% of the global mean along two-thirds of the global coastline (medium-conﬁdence). The magnitude, the rate, the timing of threshold\nexceedances, and the long-term commitment of sea level rise depend on emissions, with higher emissions leading to greater and faster rates of sea level rise. Due to relative sea level rise, extreme sea level events that occurred once per century in the recent past are projected to occur at least annually at more than half of all tide gauge locations by 2100 123 This outcome is characterized by deep uncertainty: Its likelihood defies quantitative assessment but is considered due to its high potential impact. {WGI Box TS.1; WGII Cross-Chapter Box DEEP}\n\nBased on this information, it is clear that sea level rise is unavoidable for centuries to millennia, and it will continue for thousands of years, with projected regional relative sea level rise within 20% of the global mean. The magnitude, the rate, the timing of threshold exceedances, and the long-term commitment of sea level rise depend on emissions, and higher emissions lead to greater and faster rates of sea level rise. However, the probability and rate of sea level rise is uncertain due to deep uncertainty, and it is characterized by high potential impact. Consequently, sea level rise will continue to impact coastal ecosystems, people, and infrastructure in the 21st century, and it is likely to be chronic high tide flooding and extreme flooding during storms. The range of sea level rise varies depending on the emissions scenario, and it is between 0.15 to 0.23 m under the very low GHG emissions scenario and 0.20 to 0.29 m under the very high GHG emissions scenario. The sea level rise by 2100 depends on the emissions scenario, and it is between 0.28 to 0.55 m under SSP1-1.9 and 0.63 to 1.01 m under SSP5-8.5. It is also projected"
    }
    
3. Request:
    curl --location 'http://localhost:8000/v1/api/rag' \
    --header 'accept: application/json' \
    --header 'Content-Type: application/json' \
    --data '{
      "question": "How is climate change affecting biodiversity?"
    }'
    Reponse:
    {
    "response": " * 1) Impacts on biodiversity include:\n           - Changing patterns of distribution and abundance in ecosystems\n           - Loss of habitat\n           - Changes in species interactions and relationships\n\n         * 2) Biodiversity loss may result from:\n\n           - Climate change, including the loss and fragmentation of habitats\n           - Habitat degradation, including the loss of wetlands, forests, and grasslands\n           - Changes in the distribution and abundance of key species\n           - Changes in species interactions and relationships\n           - Changes in ecosystems, including changes in species interactions and relationships\n           - Changes in the distribution of species in relation to their preferred habitats\n           - Changes in the distribution of species in relation to human activities and development\n           - Changes in the distribution of species in relation to other factors such as climate and land use changes\n           - Changes in species interactions, including the loss of keystone species and interactions with other species\n           - Changes in species interactions, including the loss of keystone species and interactions with other species\n\n         * 3) Biodiversity loss is a key driver of:\n\n           - Climate change ( high confidence )\n           - Changes in ecosystems ( high confidence )\n           - Changes in species interactions and relationships ( very high confidence )\n           - Human activities and development ( high confidence )\n           - Other drivers ( very high confidence )\n\n         * 4) Biodiversity loss can result in:\n\n           - Reduced ecosystem services, including pollination, pest control, nutrient cycling, and water filtration\n           - Increased vulnerability to climate change and other risks\n           - Reduced resilience to climate change and other stresses\n           - Decreased adaptation to climate change and other risks\n           - Increased vulnerability to other stressors, such as human activities and development\n           - Increased vulnerability to other threats, such as invasive species and habitat degradation\n           - Increased vulnerability to other threats, such as habitat loss and fragmentation\n           - Increased vulnerability to other threats, such as climate and habitat changes\n           - Increased vulnerability to other threats, such as climate and other stressors\n           - Increased vulnerability to other threats, such as climate and development\n           - Increased vulnerability to other threats, such as climate and land use changes\n           - Increased vulnerability to other threats, such as climate changes and other stressors\n           - Increased vulnerability to other threats, such as climate and human activities\n           - Increased vulnerability to other threats, such as climate and development\n           - Increased vulnerability to other threats, such as climate and land use changes\n           - Increased vulnerability"
    }