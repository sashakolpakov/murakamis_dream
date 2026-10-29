# Independent audit of the whole-source lattice and its cut

Audit, 27 October 2026. The conductor, weighted-reflection congruence
and physical cut statements hold with the conventions specified here.
This is a direct ring proof, including the source classes lost by
ambient specialization. No computational checks are needed for it.

## 1. Rings, weighted reflection and the lattice

Work in characteristic zero, with a primitive N-th root Q, N>=2.
Put

    A=k[U,U^(-1)], B=A[Y]/(Y^N-U)=k[Y,Y^(-1)],
    X=Y+Y^(-1), delta=U-U^(-1).

The ring identification uses U=Y^N. Let iota invert Y, and hence U,
and define the weighted involution

    J f=-Y iota(f).                             (1.1)

The weight is essential. Bare inversion does not fix 1-Y and would
make the proposed lattice congruence false already for that generator.
One has J^2=I and

    J(a(U)f)=a(U^(-1))J(f).                     (1.2)

Thus J is semilinear over A, not an A-linear involution on the generic
lattice. A span of J-fixed generators need not consist of globally
J-fixed vectors: U(1-Y) is an immediate example. The congruence modulo
U^2-1, rather than generic equality Jf=f, is the correct statement.

For P_n(X)=product_(r=1)^n(X-Q^r-Q^(-r)), set

    v_n=(1-Y)P_n(X), 0<=n<N,
    L=sum_(n=0)^(N-1) A v_n.                   (1.3)

The Newton polynomials P_n are monic of degrees n, so their change
of basis from 1,X,...,X^(N-1) is unit triangular. Moreover X has
degree N over k(U): its N conjugates Q^jY+Q^(-j)Y^(-1) are distinct
as rational functions. The monic Chebyshev relation
C_N(X)=U+U^(-1), of degree N, then gives

    L=(1-Y)A[X],                                (1.4)

with the displayed N generators as an A-basis. In particular L is
independent of the chosen Q despite its useful Newton basis.

## 2. A direct proof of the conductor and congruence characterization

Write R=k[X]. Since Y^(-1)=X-Y,

    B=(1-Y)R direct_sum (1+Y)R.                 (2.1)

The change from the R-basis 1,Y has determinant two. These are the
weighted J=+1 and J=-1 eigenspaces, respectively. Also iota(delta)
=-delta, so J(delta f)=-delta J(f).

If f=f_++f_- is (2.1), the condition Jf-f in delta B is equivalent
to f_- in delta B. Write f_-=delta g. Applying J and cancelling
the nonzero delta shows Jg=g. Consequently

    {f in B:Jf-f in delta B}
       =(1-Y)R+delta(1-Y)R
       =(1-Y)A[X]=L.                            (2.2)

The second equality follows from
U=(C_N(X)+delta)/2, U^(-1)=(C_N(X)-delta)/2 and
delta^2=C_N(X)^2-4. Thus A[X]=R+delta R.

For the conductor, write S_(N-1)(X) for the monic second-kind
Chebyshev polynomial satisfying
Y^N-Y^(-N)=(Y-Y^(-1))S_(N-1)(X). Then

    delta(1+Y)/(1-Y)=-(X+2)S_(N-1)(X) in R.

Equation (2.1) now gives delta B subset L. Since U is a unit,
delta B=(U^2-1)B. This proves both claimed statements:

    (U^2-1)B subset L,
    L={f in B:Jf-f in (U^2-1)B}.               (2.3)

No reduced-fiber dimension count or root interpolation is required.

## 3. The cut uses the physical derivative, not a fixed-U derivative

For f=(1-Y)g in L define

    ell(f)=g|_(Y=1,U=1)
          =-[d/dY f(Y,U=Y^N)]_(Y=1).          (3.1)

This is intrinsic in B=k[Y,Y^(-1)]. In ambient A[Y] notation, the
Euler derivation which descends to B is

    D_phys=Y partial_Y+N U partial_U,
    D_phys(Y^N-U)=N(Y^N-U).                     (3.2)

Therefore ell=-D_phys evaluated at (Y,U)=(1,1). This proves
representation independence and gives exactly

    ell(v_n)=P_n(2)=T_n(1).                     (3.3)

For a in A, ell(af)=a(1)ell(f), since f vanishes at the physical
point Y=1. Hence ell kills (U-1)L and induces a cut on L/(U-1)L.

By contrast partial_Y with U held fixed does not descend to B:
it sends the zero relation Y^N-U to NY^(N-1). Even differentiating
a preferred A-basis representative with U held fixed gives a
different functional. For example f=U^2-1 lies in L by (2.3), is
zero in B/(U-1)B, and has

    ell(f)=-2N,

whereas its canonical fixed-U derivative is zero. This does not
contradict ell((U-1)L)=0: U+1 does not lie in L.

## 4. A weighted-J-fixed class invisible in the ambient fiber

There is a sharper example using a single Newton generator. Put
d=floor(N/2). At all roots Y^N=1, the prefactor 1-Y kills Y=1,
and the P_d factors kill all other inverse pairs. Thus v_d maps
to zero in B/(U-1)B. In fact the exact identities are

    N=2d+1: v_d=-Y^(-d)(U-1),
    N=2d:   v_d=-Y^(-d)(Y+1)(U-1).             (4.1)

They follow by multiplying
X-Q^r-Q^(-r)=Y^(-1)(Y-Q^r)(Y-Q^(-r)); in the even case the
root -1 occurs twice in the paired product. Each v_d is globally
weighted-J-fixed by construction, yet

    ell(v_d)=N   if N is odd,
    ell(v_d)=2N  if N is even.                  (4.2)

For the principal complex root, this is also
P_d(2)=product_(r=1)^d 4 sin^2(pi*r/N)>0.

Thus even the weighted-fixed condition does not justify passing
to the image of L in the ambient complete fiber. The source lives
on L/(U-1)L and detects classes in the kernel of

    L/(U-1)L -> B/(U-1)B.

This is genuine normal lattice data. The cut theorem is correct
with the physical derivative and the retained lattice; replacing
either by fixed-U differentiation or ambient-fiber evaluation
would lose its nonzero source.
