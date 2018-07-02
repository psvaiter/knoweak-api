import falcon

from .utils import get_collection_page
from knoweak.models import Session, Organization, OrganizationAnalysis


class Collection:
    """GET and POST organization analyses."""

    def on_get(self, req, resp, organization_code):
        """GETs a paged collection of analyses of an organization.

        :param req: See Falcon Request documentation.
        :param resp: See Falcon Response documentation.
        :param organization_code: The code of the organization.
        """
        session = Session()
        try:
            item = session.query(Organization).get(organization_code)
            if item is None:
                raise falcon.HTTPNotFound()

            query = session\
                .query(OrganizationAnalysis)\
                .order_by(OrganizationAnalysis.created_on)

            data, paging = get_collection_page(req, query)
            for analysis in data:
                analysis.details_location = req.relative_uri + f'/{analysis.id}'

            resp.media = {
                'data': data,
                'paging': paging
            }
        finally:
            session.close()

    def on_post(self, req, resp, organization_code):
        """Creates a new analysis for the organization considering the already filled values
        for relevance, vulnerability and security threat levels in processes, IT services,
        IT assets and security threats.

        :param req: See Falcon Request documentation.
        :param resp: See Falcon Response documentation.
        :param organization_code: The code of the organization.
        """
        session = Session()
        try:
            item = session.query(Organization).get(organization_code)
            if item is None:
                raise falcon.HTTPNotFound()

            # code here

            session.commit()
            resp.status = falcon.HTTP_CREATED
            resp.location = req.relative_uri + f'/{item.id}'
            resp.media = {'data': item.asdict()}
        finally:
            session.close()


def custom_asdict(dictable_model):
    exclude = ['organization_id']
    return dictable_model.asdict(exclude=exclude)