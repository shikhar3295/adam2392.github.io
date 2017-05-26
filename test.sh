#
# subtract strings to get the project name
#
function get_project_name() {
	local venv_dir=$VIRTUALENVWRAPPER_HOOK_DIR
	local venv=$VIRTUAL_ENV

	temp_project_name=${venv#"$venv_dir"} 	# get difference between two strings
	project_name=${temp_project_name:1} 	# remove leading '/' character

	echo $project_name
	## uncomment for debugging
	# echo $venv_dir
	# echo $venv
	# echo $temp_project_name
	# echo $project_name
}

# export proj="cd ~/Documents/$(get_project_name)"
root_dir='/Users/adam2392/Documents/'
project_dir=$(get_project_name)
cd ${root_dir}/${project_dir}