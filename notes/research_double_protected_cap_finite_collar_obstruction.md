# The double-protected spectral cap does not admit the naive finite collar

Unpublished workspace local algebraic result, 31 October 2026. Root and
coherent completed full internal analytical/source-scope reviews; this is
not external peer review. This tests the literal
marked line-chart continuation, not all possible blowups or global
reductions. No representation of the whole original group, killed global
meridian, or volume conclusion is asserted.

## 1. The original cap coefficient and the remaining parameter

Use the original ordered face quartet (x,b,c,y), with protected x=b=0.
For a positive-length LEFT row the limiting degrees are

    q=(0,0,1-nu,nu), 0<nu<=1/2.

At delta=1/2, sigma=2, the sharp coefficient action is zero. Its free
nu stationarity with finite positive ordinary multipliers gives c=y.
It does not fix nu. The proposed full-fiber boundary reduction is a
separate theorem; the present obstruction does not require it. In
particular it applies to the interior range 0<nu<1/2 if subsequent
reductions exclude the terminal value.

The exact original scalar has not lost its phase. Put theta=pi/N,
d=N-1 and take i=0, 0<=j<=floor(N/2)-1. The original source identity is

    (-1)^d H_V = sum b^i c^(d-j)
                   (prod_(a<i)alpha_a)(prod_(a>j)alpha_a) K_(i,j),
    alpha_a=2cos((2a+1)theta)-sigma.

At x=0, K_(0,j)=y^j prod_(a=1)^j 4sin^2(a theta). At sigma=2 every
unused alpha_a=-4sin^2((a+1/2)theta)<0. Consequently the RAW coefficient
of c^(d-j)y^j in H_V is (-1)^j A_j, where

    A_j=csc^2(theta/2)
            prod_(a=1)^j sin^2(a theta)/sin^2((a+1/2)theta)>0. (1)

Indeed prod_(a=0)^d 4sin^2((a+1/2)theta)=4. This is valid at both
parities and retains the original omitted half. The signed output clock
c_tilde=-c makes (-1)^j c_tilde^(d-j)=(-1)^d c^(d-j), a common recorded
sign; it is precisely the post-pole sign choice, not deletion of the
j-dependent phase. Thus c=y corresponds to the signed middle q=-y
in the existing reflection chart. This does not by itself impose a
global face-sign solution.

## 2. Literal raw reflections at the cap

Use the matrices in the [literal signed line flags](research_signed_spectral_line_flags.md),
section1. An anti-Mobius reflection is represented by J with det J=-1;
ordered products are J_2 conjugate(J_1). Put s=sin(pi delta),
k=cos(pi delta). The protected outer line and ordinary outer circle are

    J_x=-i I,
    J_y=[[i cos(2pi delta),sin^2(2pi delta)/y],
         [y,i cos(2pi delta)]].

For signed middle q and its actual root T_q^2=qy+q^2 s^2,

    J_q=[[i-2kT_q/y,-4k^2(y+q s^2)/y^2],
         [q,i+2kT_q/y]].                              (2)

At the protected input b=0, T_b=0 and
J_b=[[i,-4k^2/y],[0,i]]. These are the actual two marked line lifts;
their height is 2k^2/y. Define, with the ORIGINAL head order,

    A_q=J_q conjugate(J_x), B_q=J_y conjugate(J_q),
    P=B_q A_q=J_y conjugate(J_x).                     (3)

Now set delta=1/2, c=y, q=-y directly in the polynomial matrices (2).
All entries are finite, without any division by T or k:

    J_x=-iI, J_b=iI,
    J_y=[[-i,0],[y,-i]], J_q=[[i,0],[-y,i]]=-J_y,
    P=[[1,0],[iy,1]]!=I.

Direct multiplication in (3) gives

    (A_b,B_b)=(-I,-P),
    (A_q,B_q)=(-P,-I).                               (4)

Thus there is NO finite invertible C with

    C A_b C^(-1)=A_q, C B_b C^(-1)=B_q.              (5)

The first equality would conjugate the central matrix -I to the
noncentral matrix -P. This obstruction remains in PSL2: identity cannot
be conjugated to a nontrivial parabolic. Changing central lifts or adding
decorating flags does not alter that central/noncentral distinction.

The coincident marked lines therefore do not give a finite specialization
of the proved original collar. The negative output circle is the same
projective circle as y, and the central MAIN head has moved to the other
ordered leg. Merely listing matching traces or free fixed flags cannot
repair the required simultaneous ordered conjugations.

## 3. An exact family exposes the singular collar

There is a useful diagnostic family with the SAME protected faces, even
though its terminal row need not be among the surviving global maxima.
For 0<delta<1/2 set c=y/s^2 and take q=-c,T_q=0. The local endpoint
equations then have nu=1/2, and the existing centralizer has R0=-1.
Write h=sin(2pi delta)>0. In the ORIGINAL frame its projective matrix is

    C=[[0,-h/y],[-y/h,0]], C^2=I.                   (6)

For example,

    A_b=[[-1,-4ik^2/y],[0,-1]],
    A_q=[[-1,0],[-iy/s^2,-1]],

and (6) conjugates A_b to A_q since h^2=4s^2k^2. It commutes with
the whole ordered P, so it conjugates B_b to B_q as well. Its
projective determinant is -1; choosing a determinant-one central lift
does not change any conclusion.

As delta approaches1/2, (6) has no invertible projective limit: multiply
by h/y to obtain a matrix tending to [[0,0],[-1,0]], of rank one.
This is the explicit mechanism behind (4), not an arbitrary failure of
continuity at collided ideal vertices. The marked-strip height collapses
while the noncentral outer product remains noncentral in this frame.

Imposing the free-spectral critical endpoint equations with x=b=0
forces nu=1/2, outside the strict nonterminal stratum. At the cap the exact monomer permits
arbitrary nu. Hence (6) does not approximate arbitrary cap loads by actual
regular marked critical data. In the direct cap circle matrices the
parameter nu has disappeared; any recovery of it needs additional
boundary data rather than an unproved assignment of angles to coincident
centers.

## 4. Exact limitation

This refutes only the naive finite-collar extension of the existing
line/reflection chart, with its original ordered heads and retained signed
clock. It does not refute a different blowup, a global block reduction,
or cancellation of the original cap source. A parameter-dependent common
conjugation may change which limiting heads remain noncentral, and needs
its own whole-source flags and sewing analysis. No such operation is
assumed here.

In particular (4) is NOT a global group representation: its required
local relation already fails. The central input therefore cannot be
called a killed meridian in an established representation, and no
representation-volume gap follows from it. The existing regular
fundamental-chain theorem must not be applied at this cap merely because
the local sharp action is zero or the marked lines coincide.

Dependencies: the [original four-state source](research_original_one_sided_four_state_transfer.md)
for the exact finite sign, the [literal signed line flags](research_signed_spectral_line_flags.md)
for (2)--(3), and the [regular stationary reduction](research_regular_shared_spectral_stationary_reduction.md)
for the terminal strict-critical restriction.

Both internal reviews checked the exact coefficient and both parity signs,
the signed-clock convention, original ordered anti-Mobius products,
central/noncentral obstruction, explicit conjugator and its singular
projective limit. The scope excludes arbitrary blowup gauges, a global
group representation, any killed global meridian or a volume conclusion.
The calculations are explicit two-by-two identities; no numerical audit
is claimed.
