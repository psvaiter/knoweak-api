from controllers import extensions, department, macroprocess, process, \
                        it_service, it_asset, it_asset_category, \
                        organization, organization_department, organization_macroprocess, \
                        organization_process, organization_it_service, organization_it_asset, \
                        system_user, system_user_role


def configure_media_handlers(api):
    json_handlers = {
        'application/json': extensions.JSONHandler(contract_in_camel_case=True),
        'application/json; charset=UTF-8': extensions.JSONHandler(contract_in_camel_case=True)
    }
    api.req_options.media_handlers.update(json_handlers)
    api.resp_options.media_handlers.update(json_handlers)


def configure_routes(api):
    # Add routes for domain data
    api.add_route('/departments', department.Collection())
    api.add_route('/departments/{department_id}', department.Item())
    api.add_route('/macroprocesses', macroprocess.Collection())
    api.add_route('/macroprocesses/{macroprocess_id}', macroprocess.Item())
    api.add_route('/processes', process.Collection())
    api.add_route('/processes/{process_id}', process.Item())
    api.add_route('/itServices', it_service.Collection())
    api.add_route('/itServices/{it_service_id}', it_service.Item())
    api.add_route('/itAssets', it_asset.Collection())
    api.add_route('/itAssets/{it_asset_id}', it_asset.Item())
    api.add_route('/itAssetCategories', it_asset_category.Collection())
    api.add_route('/itAssetCategories/{it_asset_category_id}', it_asset_category.Item())

    # Add routes to handle organizations and their sub-resources
    api.add_route('/organizations', organization.Collection())
    api.add_route('/organizations/{organization_code}', organization.Item())
    api.add_route('/organizations/{organization_code}/departments', organization_department.Collection())
    api.add_route('/organizations/{organization_code}/departments/{department_id}', organization_department.Item())
    api.add_route('/organizations/{organization_code}/macroprocesses', organization_macroprocess.Collection())
    api.add_route('/organizations/{organization_code}/macroprocesses/{macroprocess_instance_id}', organization_macroprocess.Item())
    api.add_route('/organizations/{organization_code}/processes', organization_process.Collection())
    api.add_route('/organizations/{organization_code}/processes/{process_instance_id}', organization_process.Item())
    api.add_route('/organizations/{organization_code}/itServices', organization_it_service.Collection())
    api.add_route('/organizations/{organization_code}/itServices/{service_instance_id}', organization_it_service.Item())
    api.add_route('/organizations/{organization_code}/itAssets', organization_it_asset.Collection())
    api.add_route('/organizations/{organization_code}/itAssets/{asset_instance_id}', organization_it_asset.Item())

    # Routes for system management and access control
    api.add_route('/management/users', system_user.Collection())
    api.add_route('/management/users/{user_id}', system_user.Item())
    api.add_route('/management/userRoles', system_user_role.Collection())
    api.add_route('/management/userRoles/{user_role_id}', system_user_role.Item())