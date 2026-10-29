# The actual braid transport has a semisimple sector

Research note, 26 October 2026. The finite-by-Heisenberg result
for ideal shape ordering does not extend to the full actual
braid-source transport. At every level the latter has a
connected subgroup with an SL_2 quotient. We prove this from
the prescribed crossing, using a nonzero exact pivotal moment
and an ordinary-trace identity with definite sign. Finite-index
restriction cannot remove that sector.

This suggests a relative approach: retain the semisimple
central/spectral algebra and study its normalization or period
extension. We give an explicit rank-four algebra for the two
unipotent generators, and show how the already computed actual
two-channel source splits on a quadratic spectral cover.
Neither construction identifies its spectral coordinate with
the geometric A-curve or proves the volume conjecture.

## 1. Fix the actual crossing and its phase

Let N>=2, q=exp(pi*i/N), Q=q^2, rho=q-q^(-1), and use exactly
the actual color V=V_(x_0), x_0=q^(N-1)=-q^(-1). Write B for
the checked crossing with the common Cartan scalar removed,
as in the original ADO cut. Its zero-framing scalar is

    theta=x_0^(1-N), theta^(2N)=1.

Replacing B_i by theta^(-1)B_i gives the same zero-framed
word evaluation and is still a braid representation. Thus
the pure braid powers below are the actual normalized ones:

    U_1=B_12^(2N)=I+X,
    U_2=B_23^(2N)=I+Y,
    J=B^(2N)-I, X=J tensor I, Y=I tensor J.       (1.1)

For the full universal crossing the common scalar and twist
cancel in this same normalization. No peripheral or modified
dimension factor is changed.

The [independently proved Casimir interpolation](casimir_braiding_and_recoupling_lattice.md#3-the-actual-crossing-has-a-unique-confluent-polynomial)
has double nodes c_k=q^h+q^(-h), h=2k+1<N, with

    r_N(c_k)=nu_k=(-1)^k q^(k(k+1)),
    r_N'(c_k)/nu_k=-(N-h)/[2(q^h-q^(-h))].

The one possible simple node has the same root-of-unity
property nu_k^(2N)=1. Since B=r_N(Omega), (1.1) obeys

    J^2=0, X^2=Y^2=0.                            (1.2)

The claim follows by evaluating the value and derivative
of (r_N^(2N)-1)^2 at every double node; both are zero.
The same polynomial vanishes at the simple node. This is
a statement about the actual matrices, not a formal leading
symbol or a spectral projector substituted for a crossing.

## 2. An exact nonzero pivotal moment

Keep the original K and pivot g=K^(1-N)=(-1)^(N-1)K. The
already proved closing functional on the Casimir algebra is

    ptr_K f(Omega)
      =[-sum_(h odd, 0<h<N)
          (c_h f(c_h)+(q^h-q^(-h))^2 f'(c_h))
                      + simple-node contribution] I.

For f=r_N^(2N)-1 its node values are zero and its double-node
derivatives are -N(N-h)/(q^h-q^(-h)). Therefore, exactly,

    ptr_K J=Phi_N I,
    Phi_N=N sum_(h odd, 0<h<N)(N-h)(q^h-q^(-h))
                         =-2N^2/rho !=0.          (2.1)

For the last equality multiply the sum by rho and use

    rho(q^h-q^(-h))
       =(q^(h+1)+q^(-h-1))-(q^(h-1)+q^(-h+1)).

The weighted sum telescopes; q^N=-1 and the Q-geometric sum
give -2N, for either parity of N. Thus no exceptional level
or unverified noncancellation hypothesis enters (2.1).

With the actual pivot the corresponding scalar is

    L_N=(-1)^(N-1) Phi_N.

Sequentially closing strands 3 and 2 in XY gives

    t_reduced,W(XY)=L_N^2,
    mathfrak_t_W(XY)=d_N(1)L_N^2 !=0,
    d_N(1)=i^(N+3)/N.                           (2.2)

These are the actual cut and its full modified normalization.
This test uses the pure-braid source operators; the braid
powers depend on N. It is not the fixed-knot volume limit.

## 3. A negative ordinary trace forces a semisimple quotient

For a pair matrix use the total integer degree a+b. The
actual B and J preserve that degree, so the ordinary partial
traces

    A=Tr_1 J, C=Tr_2 J

are diagonal. We claim C=-conjugate(A). Here is a direct
proof retaining the original Cartan order. Write B=P D Theta,
where P is the swap and

    D_(a,b)=x_0^(-a-b)q^(2ab).

In this color E_j=[j]_q^2 is real and F is the real unit
shift. Complex conjugation of the finite Euler coefficients
gives Theta^(-1), while conjugation gives D^(-1) on D.
The finite inverse identity is the ordinary Euler convolution
on its nilpotent argument. Hence

    conjugate(B)=D^(-1) P B^(-1) P D,
    conjugate(J)=-D^(-1) P J P D.               (3.1)

The second equation uses J^2=0. On diagonal entries the D
factors cancel. Summing the diagonals gives C=-conjugate(A).
Consequently on W=V^(tensor 3),

    Tr_W(XY)=Tr(A C)=-sum_a |A_aa|^2 <0.         (3.2)

The strict inequality has a proof, not a numerical assumption:

    Tr(A K)=Tr[J(I tensor K)]=N Phi_N !=0.

Indeed (2.1) computes this trace by closing the other factor.
As |K_aa|=1, it also gives the quantitative bound

    -Tr_W(XY) >= N |Phi_N|^2=4N^5/|rho|^2.       (3.3)

Now XY has a nonzero eigenvalue lambda. Choose v with
XYv=lambda v and put w=Yv. Then

    Xv=0, Xw=lambda v, Yv=w, Yw=0.

The vectors v,w are independent. Their plane is invariant
under U_1,U_2, with matrices

    U_1|=[1 lambda;0 1], U_2|=[1 0;1 1].         (3.4)

Their cyclic powers are Zariski dense in the respective
one-parameter upper and lower unipotent groups, since the
characteristic is zero. Those two groups generate SL_2:
elementary upper/lower row operations give its open Gaussian
cell and its remaining matrices. Thus the closure of the
subgroup generated by U_1,U_2 has an SL_2 quotient on this
plane and lies in the identity component of the full braid
image closure.

In particular that identity component is not solvable, and
is not nilpotent. Every finite-index subgroup of the original
braid group contains positive powers of both pure braids.
The same plane argument applies with their two nonzero
parameters rescaled. Thus no such restriction removes this
connected semisimple sector, at any N>=2.

The invariant plane here is selected from an eigenvalue of
XY; it is not asserted to be the two-cup corner. That corner
is not generally preserved by the full braid powers. Nor
does this theorem compute the difference-Galois group of
the minimal quantum A-operator or identify its selected
geometric branch. It tests the full retained braid transport,
which is stronger data than a normalization line.

## 4. The two-square-zero algebra has an explicit spectral center

There is nevertheless a useful reduction. In the universal
algebra on X,Y with X^2=Y^2=0, put

    c=XY+YX.

It commutes with both generators. Every alternating word
reduces to a C[c]-linear combination of 1,X,Y,XY; for example
(XY)^k=c^(k-1)XY and XYX=cX. These four elements are independent,
as the following model over C[c] shows:

    X=[0 1;0 0], Y=[0 0;c 0], XY=[c 0;0 0].

Its commutator equations also show that the center is exactly
C[c]. After c is inverted the algebra is Mat_2(C[c,c^(-1)]),
with matrix units

    e_11=XY/c, e_22=YX/c, e_12=X, e_21=Y/c.      (4.1)

Thus on a simple nonzero spectral component the comparison
problem reduces to a line. Replacing a source module by only
its scalar center still loses its multiplicity, lattice and
period functional; those remain specified data.

At c=0 the flat abstract fiber is the four-dimensional
exterior algebra X^2=Y^2=0, YX=-XY. Its augmentation ideal
has cube zero, and

    [1+sX,1+tY]=1+2stXY

is central. This is the two-step nilpotent fiber. The ambient
two-by-two matrix specialization of the displayed model is
not faithful there; using it alone would lose the flat source
directions. A finite field extension cannot send a nonzero
spectral value c to this zero fiber.

For the actual X,Y of (1.1), (3.2) proves that nonzero spectral
components occur. The spectral center is for this pair of
pure powers. It is not claimed to commute with the original
B_12,B_23, or to give their entire knot-period decomposition.

## 5. The actual cap source detects its matrix sector

There is also a completely calibrated source test. Use the
actual adjacent cups and caps from
[the source normal form](adjacent_source_normal_form.md#1-adjacent-cups-and-caps-give-opposite-source-matrix-units).
Their operators Pi_1,Pi_2 have square zero and obey

    Pi_1 Pi_2 Pi_1=Pi_1, Pi_2 Pi_1 Pi_2=Pi_2.

Their common corner is two copies of V. On it they are
E_12,E_21, with the actual full modified trace
d_N(1) times the ordinary two-by-two trace. Let

    A_s=I+s Pi_1, B_t=I+t Pi_2,
    C_(s,t)=A_s B_t A_s^(-1) B_t^(-1).

On the corner det C=1 and Tr C=2+s^2t^2, and it is the
identity on the complementary source. Therefore, exactly,

    mathfrak_t_W(C_(s,t)^m-I)
       =d_N(1)[T_m(2+s^2t^2)-2],                 (5.1)
    T_0=2, T_1=z, T_(m+1)=zT_m-T_(m-1).

This follows from the actual rectangular trace calibration,
not from choosing a new scalar trace. For s=t=1 the trace
argument is 3, so the right side detects the semisimple
matrix dynamics. These localized source units need not be
braid words; (3.4) supplies the separate genuine-braid theorem.
Growth in m in (5.1) concerns word length at a fixed N, not
growth of a fixed knot as the level changes.

## 6. A cover can split the spectral algebra instead of killing it

The original meridian source already has the appropriate
quadratic deformation. Its two numerators satisfy

    t_1^2=delta t_1, t_2^2=delta t_2,
    z=t_1t_2+t_2t_1-delta(t_1+t_2) central.

On the actual charged two-copy block,

    delta=rho(M^2-M^(-2)),
    A_N=(-1)^N rho(M+M^(-1))
             *(qM^2-q^(-1)M^(-2))/(M^N+M^(-N)),
    z=A_N^2-delta^2.                             (6.1)

All functions are the previously calibrated actual ones.
In particular the peripheral denominator is retained. More
generally pass to the quadratic cover A^2=z+delta^2. Where
A and z are units, the identities

    e_11=(t_1t_2-delta t_1)/z,
    e_22=(t_2t_1-delta t_2)/z,
    e_12=(t_1-delta e_11)/A,
    e_21=(t_2-delta e_22)/A                     (6.2)

are matrix units, directly splitting this rank-four algebra.
The actual mark is A=A_N, and at completeness A_N=(-1)^N rho^2
is nonzero. Thus the meridian source is on the matrix-algebra
locus at each fixed level, rather than at its nilpotent fiber.

Once these source generators and the charged simple module
are matched, their simultaneous comparison is a scalar line.
This is a useful finite-cover reduction of a torsor problem.
It preserves the semisimple algebra, its integral source and
its trace, while making the remaining comparison rank one.
It does not prove that the same central functions and cut
are realized on the geometric triangulation or A-curve.

This statement concerns the integral numerators t_i. It does
not supply a common finite lattice for both unscaled
projectors t_i/delta; their double-pole trace obstruction
from the adjacent-source note remains in force.

## 7. Consequence for the Regge and cover strategy

The [finite Regge/ordering result](regge_period_covers_and_a_curves.md)
and its Heisenberg period kernel remain valid. The present
theorem rules out extending that nilpotence claim to the
whole actual braid-source group. A finite cover can still
choose roots, split a spectral algebra and make scalar
comparison possible, as (6.2) shows. The target must keep
the semisimple source and seek a controlled period extension
or marked quotient over it.

Such a relative viewpoint has existing coverage in
[Hain's relative Malcev theory](https://arxiv.org/abs/alg-geom/9607019).
Also, the stated homological model of
[De Renzi--Martel, 2212.10940](https://arxiv.org/abs/2212.10940)
uses Heisenberg coefficients for quantum mapping-class-group
representations. A nilpotent coefficient group does not assert
that the represented mapping class or braid image is nilpotent.
[Karvounis, 1909.11162](https://arxiv.org/abs/1909.11162)
already treats projective quantum-sl2 braid representations
and nontrivial central action. Only their stated coverage
was consulted; none of their proofs is used above.

We have not identified the SL_2 plane of (3.4) with hyperbolic
holonomy, built the requisite relative completion of the
selected quantum A-period, or proved its regulator norm.
The original conjecture remains unproved.

[The audit](../experiments/audit_actual_semisimple_transport.py)
checks the genuine pure powers, the conjugation and pivotal
identities, full original source closings, and the spectral
matrix-unit and commutator formulas.
[Results](../experiments/actual_semisimple_transport_results.json).

Reproduce with:

    python3 experiments/audit_actual_semisimple_transport.py
