set(dataset_path ${CMAKE_CURRENT_SOURCE_DIR}/downloads CACHE PATH "The path to store datasets to")

SET(DATASET_ARGS "--delete_original" CACHE STRING "CLI args for the dataset script, defaults to --delete_original")

macro(dataset_target dataset_name dataset_config)
    add_custom_target(${dataset_name}
        COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/get_datasets.py ${dataset_path} ${CMAKE_CURRENT_SOURCE_DIR}/${dataset_config} ${DATASET_ARGS}
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    )
    set_target_properties(${dataset_name} PROPERTIES EXCLUDE_FROM_ALL true)
endmacro(dataset_target)

dataset_target(datasets       datasets_config.py)
dataset_target(large_datasets large_datasets_config.py)
