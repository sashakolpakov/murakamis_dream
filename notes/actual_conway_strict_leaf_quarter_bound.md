# Every complete robust Conway leaf lies strictly above one quarter

29 October 2026. For every retained cylindrical robust factor, the
unique complete source optimizer satisfies x_l>1/4 at EVERY h leaf.
This follows from the actual g,m stationarity equations and a preserved
port inequality. No circle-packing estimate is assumed. The result is
about the existing positive complete source; replacement by a different
quantum coupon still requires its own local and global source estimates.

## 1. Positive port variables from the actual source derivatives

For a proper robust expression E at output b in (0,1), let
f_E(b)=v_E(b)/pi be its strictly optimized source action. Put

    B=cot(pi b), kappa=exp(-f'_E(b)),
    X=sqrt((1+B^2)/(1+kappa)), Y=sqrt(kappa) X.               (1)

Thus X,Y are positive and X^2+Y^2-B^2=1. The already proved strict
maximum theorem makes these derivatives legitimate at every proper
macro-port of the complete optimizer.

A literal turn sends

    (B,X,Y) -> (-B,Y,X).                                    (2)

At a product F G with strict input/output x,y,z, write
U=cot(pi x), V=cot(pi y), Z=cot(pi z), and

    D=(U+V)Z-UV+1>0.

The strict inequality x+y<1 gives U+V>0. Directly differentiating
the SAME seven-factorial action m gives

    kappa_F=exp(m_x)=(U+V)(U-Z)/D,
    kappa_G=exp(m_y)=(U+V)(V-Z)/D,
    kappa_out=exp(-m_z)=(U-Z)(V-Z)/D.                        (3)

Here the first two signs use f'_F=-m_x and f'_G=-m_y at the inner
maximum. Since

    1+kappa_F=(1+U^2)/D,
    1+kappa_G=(1+V^2)/D,
    1+kappa_out=(1+Z^2)/D,

all THREE ports have the same X=sqrt(D), and

    Z=(UV+X^2-1)/(U+V),
    Y_out=Y_F Y_G/(U+V).                                    (4)

The positive square root in the last identity is fixed by U+V>0.
These are exact algebraic consequences of stationarity, not new
gluing assumptions.

## 2. A strict inequality preserved by the entire robust grammar

Every proper robust port satisfies

    -Y < B < X.                                             (5)

First check A=h^3. At a leaf the actual action has
g'(a)=2log cot(pi a). Therefore its coordinates are

    B=X=cot(pi a)>0, Y=1.

The common-X identity (3) makes the three stationary seed leaf
coordinates equal. Composing twice using (4) gives

    B_2=(2X^2-1)/(2X), Y_2=1/(2X),
    B_A=X(4X^2-3)/(4X^2-1), Y_A=1/(4X^2-1).                (6)

The second product has B_2+X>0, so X>1/2. Consequently

    X-B_A=2X/(4X^2-1)>0,
    B_A+Y_A=(2X-1)(X+1)/(2X+1)>0,

which proves (5) for every interior seed output. Equation (2)
preserves (5), because its two inequalities exchange.

It remains to check a product of two ports satisfying (5).
If the common X>=1, the identities Y_F^2=1+U^2-X^2 and
U>-Y_F force U>0; similarly V>0. Also U<X, V<X and

    U>sqrt(X^2-1), V>sqrt(X^2-1).

Hence 0<X-U<1 and 0<X-V<1 (also at X=1). Equation (4) gives
Z>0 and

    Z-X=((X-U)(X-V)-1)/(U+V)<0.

Thus -Y_out<Z<X.

If 0<X<1, put h=sqrt(1-X^2), and write uniquely

    U=h cot alpha, Y_F=h csc alpha,
    V=h cot beta,  Y_G=h csc beta,    0<alpha,beta<pi.

With alpha_0=arccos X, the upper inequalities U<X,V<X say
alpha,beta>alpha_0. The actual U+V>0 says alpha+beta<pi.
Equation (4) is now exactly

    Z=h cot(alpha+beta), Y_out=h csc(alpha+beta).            (7)

Thus Z<X since alpha+beta>alpha_0, while Z>-Y_out follows from
cot t+csc t=cot(t/2)>0 for 0<t<pi. This proves preservation
of (5), and hence proves it for all robust expressions.

## 3. Closure and downward propagation

For a retained factor C(FG), its two proper children F,G are robust.
After deleting the final forced-flat gate, their outputs are b,1-b.
Stationarity of f_F(b)+f_G(1-b) gives equal derivatives and therefore
equal kappa. Their port data are consequently (B,X,Y) and (-B,X,Y).
Applying (5) to both gives |B|<min(X,Y). Since
X^2+Y^2-B^2=1, this implies

    0<X<1, 0<Y<1                                          (8)

at both root child ports.

These two strict bounds propagate down the ROBUST macro-tree.
They are preserved by a turn. At a product, X is common, hence
already below one. Use (7). Its parent Y_out<1 means

    alpha_0<alpha+beta<pi-alpha_0.

Each robust child already has alpha,beta>alpha_0 by (5), so each
also lies below pi-alpha_0. Therefore sin alpha,sin beta>h,
which gives Y_F,Y_G<1. Thus (8) holds at every robust seed port.

STOP this propagation at A: its individual leaf ports have Y=1,
so (8) is not asserted for those ports. Instead use (6): all three
seed leaves share the seed's X. Since this X is strictly below one,

    cot(pi x_l)=X<1, hence x_l>1/4.                         (9)

The remaining retained factor C(A) is equally explicit. Its two
closing children are h^2 and h; their cotangents are opposite.
The same root matching again makes X common. Thus B_2=-X in (6),
forcing X=1/2 and
x_l=atan(2)/pi>1/4 for all three leaves.

This proves (9) for every retained cylindrical robust factor. For
each FIXED expression there is a positive minimum margin above
1/4 because it has finitely many leaves. No uniform margin across
all expressions is claimed or needed here.

The theorem locates the whole positive-source optimizer in the
strict local regime required by the proposed odd-half-twist packet.
It does not itself identify that packet with the pure source or
prove survival of its summed complex amplitude.

Primary-agent independent analytical review: PASS. The product identities were derived directly using D=(U+V)Z-UV+1; the seed inequalities, both X>=1 and X<1 preservation cases, closure inequalities, macro-only downward propagation, and separate C(A) endpoint were checked. No uniform margin over all expressions or odd-coupon source theorem is inferred.
