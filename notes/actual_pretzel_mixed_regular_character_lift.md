# The selected mixed pretzel packet has an explicit regular character lift

29 October 2026. This identifies the regular algebraic branch selected by
the original mixed inner source with an explicit auxiliary meridian. It
does not identify a representation by matching cusp Hessians. The source
Riccati ratio fixes the internal critical root, the literal factorial
ratios fix its two remaining conjugate variables, and a two-by-two matrix
calculation realizes the resulting disk-product character. The literal
quarter-turn port identification and global concatenation are supplied
separately; neither a trace equation alone nor this local calculation is
being substituted for that gluing proof.

## 1. Recover the internal critical point from the selected finite source

Use the exact original mixed sums, normalizations, and source endpoint in
[the mixed inner theorem](actual_pretzel_mixed_inner_source_wkb.md):

    A_(h,r)=sum_(v=r)^M Q^(-vr) F_(2v)/
                  [F_v F_(v-h) F_(v+h) F_(v-r)],
    D_(h,r)=Q^(-r^2) F_(2r)/[F_r F_(r-h) F_(r+h)],
    U_(h,r)=A_(h,r)/D_(h,r).

Here r is in its fixed high window, h is in the small cusp corridor,
H=Q^h, Y=Q^r, and the prescribed factorial completion is used for complex
h. In particular no arbitrary solution of the Ward equation is chosen.
The exact source has U_M=1 and its last backward coefficient vanishes.
Its proved selected ratio tends to the simple dominant root mu of

    mu^2-p mu-q=0,
    den=(1-Y/H)(1-YH),
    p=-Y^(-1)[(H+H^(-1))Y^2+2]/den,
    q=-Y^(-2)(1-Y^2)^2/den^2.                         (1)

The adjacent D ratio has the limit

    d(Y,H)=Y^(-2)(1-Y^2)(1+Y)/den.

There is also a literal, exact moment identity. The ratio of the v-th
summand of A_(h,r+1) to that of A_(h,r) is

    Q^(-v)-Q^(-r).

The v=r endpoint on the second sum is zero, so this holds after summing,
with no missing boundary term. Consequently the effective internal root
selected by that source is

    X^(-1)=Y^(-1)+d(Y,H)/mu,
    X=Y mu/[mu+Yd(Y,H)].                             (2)

Substitution of (2) in (1), followed by clearing its regular
denominators, gives precisely

    (Y+T+1)X^2-(TY+2)X+Y-1=0, T=H+H^(-1).          (3)

This equivalence is algebraic on the stated regular chart. At H=1 the
SOURCE-selected root mu=-Y^(-1) gives

    X=(Y-1)/(Y+3),

rather than the other normalized channel. Thus (2) also fixes the
branch on a small complex neighborhood by holomorphic continuation.
All denominator exclusions in (1)--(3) are retained.

## 2. Literal phase and its conjugate coordinates

The complete phase S_0 is the finite-factorial phase in
[the independent symbol audit](actual_pretzel_geometric_symbol_audit.md).
The exact mixed summand changes it by

    S=S_0-2Li2(X)+Li2(X/H)+Li2(XH)+(Log H)^2/2.       (4)

The last term is the original q^(h^2) factor, not an adjustable
flattening. The original common kappa and all quarter-turn phases remain
as in the source theorem. Differentiating the actual product-log chart
gives

    exp(S_x)=(1+X)^2(X-1)/[(X-Y)(1-X/H)(1-HX)],
    exp(S_y)=(1-Y/X)(1-wY)(1-Y/w)/(1-Y)^3,
    U=exp(S_t)=(wY-1)/(w-Y),
    L=exp(S_LogH)=(H-X)/(1-HX),                       (5)

where x=Log X,y=Log Y,t=Log w. Equation exp(S_x)=1 is exactly
(3). The second equation exp(S_y)=1 is

    (1-Y/X)[1-(w+w^(-1))Y+Y^2]=(1-Y)^3.             (6)

On the regular branch the same integer inner mark as in the complete
source is retained by continuation. Equations (5)--(6) do not erase
that mark. They identify the exponentiated critical coordinates; the
marked primitive remains the one fixed by the finite source.

The displayed L is also fixed directly by the exact physical h-shift:
the original q^(h^2), F_(v-h), F_(v+h) factors have limiting ratio

    H(1-X/H)/(1-HX)=L.

Thus no undetermined square root of an auxiliary longitude is inserted.
The auxiliary physical meridian is M=H^(-1/2), with branch M=1 at h=0.
A positive physical-color/meridian shift reverses the h-shift. Its
preferred longitude marking also retains the original ordinary-circle
pivot sign. The [typed longitude certificate](actual_mixed_crossing_circle_preferred_longitude.md)
proves that the preferred M-eigenflag longitude is precisely -L^(-1).

## 3. The dual Casimir is an actual four-punctured trace

The literal quarter-turn dual-Casimir operator in
[the original alias theorem](actual_pretzel_mixed_alias_source_gap.md)
has principal symbol

    D(w,U)=((w-1)/(w+1))^2(U+U^(-1))+8w/(w+1)^2.     (7)

This symbol has an explicit trace realization. Put t=(w-1)/(w+1),
P_0=diag(w,w^(-1)), and define

    mu_1=[[2w/(w+1),1],[-t^2,2/(w+1)]],
    mu_2=P_0 mu_1^(-1),
    mu_3=[[2/(w+1),wU],[-t^2/(wU),2w/(w+1)]],
    mu_4=(mu_3 mu_2 mu_1)^(-1).                     (8)

Each matrix has determinant one and trace two. Their ordered product
is I, and direct multiplication gives

    Tr(mu_2 mu_1)=w+w^(-1),
    Tr(mu_3 mu_2)=D(w,U).

For w not in {0,1,-1} and U!=0 this tuple is irreducible: the first
pair alone has distinct fixed flags. This is an explicit character
lift, rather than an inference from the dimension of a trace variety.

Substituting (5) and using (3),(6) gives the exact identity

    D(w,U)=-(L+L^(-1)).                              (9)

For a reproducible rational verification, solve (3) as

    Y=[1+2X-(T+1)X^2]/[1-TX+X^2],

then solve (6) for w+w^(-1); substitute these in (7). No equation
at a collision divisor is canceled and then reintroduced as a regular
solution. At completeness D=-2 although L=1; the central minus sign
in (9) must therefore be retained.

## 4. A framed auxiliary meridian, including its parabolic limit

Let P be the actual unrotated disk-product matrix, with determinant
one and trace D in (9). Define

    beta=-(H-X)(1-HX)/[sqrt(H)(H+1)(1-X^2)],
    C=beta(P-YI).                                    (10)

All square roots are the branch through H=1. Equations (3),(9) imply

    det C=1, Tr C=sqrt(H)+1/sqrt(H), [C,P]=0.          (11)

More precisely, on the P-eigenflag with eigenvalue lambda=-L^(-1),
C has eigenvalue M=H^(-1/2); on the reciprocal flag it has M^(-1).
These assertions follow by the scalar identities

    beta(lambda-Y)=H^(-1/2),
    beta(lambda^(-1)-Y)=H^(1/2).

The formula has a removable complete-color degeneration. At H=1,
equation (3) on the selected branch gives Y=(1+3X)/(1-X), so

    C=I-(P+I)/(1+Y), Tr P=-2.                        (12)

For noncentral P this is a NONCENTRAL trace-two unipotent. Thus the
auxiliary meridian does not collapse to I merely because its eigenvalue
becomes one. Formula (10) is finite in a bounded port frame at this
limit, although a frame diagonalizing P becomes singular there.

Here is a direct tangle test. For actual meridians a,b,C, put P=ba.
The positive Hurwitz convention is (a,b)->(a^(-1)ba,a). The literal
auxiliary threading word [2,1,1,2] sends the auxiliary meridian to
P^(-1)CP. Closing that physical auxiliary component is therefore
EXACTLY [C,P]=1; under this condition the main outputs are

    (C^(-1)aC,C^(-1)bC).

Following it by the retained negative half twist gives

    r=C^(-1)bC, s=C^(-1)bab^(-1)C.                  (13)

For generic H!=1 diagonalize P as diag(lambda,lambda^(-1)), with
lambda=-L^(-1), and set t_lambda=(lambda-1)/(lambda+1). One may take

    a=[[2lambda/(lambda+1),1],
                         [-t_lambda^2,2/(lambda+1)]],
    b=P a^(-1), C=diag(M,M^(-1)).

Then (13) gives

    Tr(r^(-1)a)=2-t_lambda^2
                      [2+lambda H+lambda^(-1)H^(-1)]. (14)

Substitution of L=(H-X)/(1-HX) and the two actual stationary
equations (3),(6) makes (14) exactly w+w^(-1). Thus the selected
factorial branch satisfies the mixed threaded-half-twist character
relation, with the original auxiliary meridian and a specified flag.
The regular formula (10), not this singular diagonal frame, is used
at H=1.

## 5. Scope of the local certificate

This proves a source-selected regular local character lift and an
explicit auxiliary-meridian matrix. The additional literal quarter-turn
ordering, conjugating frames, and global source/cap equations are proved
in [the global port theorem](actual_pretzel_port_lift_and_geometric_anchor.md).
The [preferred-longitude certificate](actual_mixed_crossing_circle_preferred_longitude.md)
retains its sign and framing. The
[marked action comparison](actual_pretzel_marked_regulator_and_filling_action.md)
then identifies the source action with the regulator of the extended
filled representation. These separately proved steps are not inferred
from matching a cusp Hessian. They give a representation-volume upper
bound; identifying the deformed representation as the filled geometric
holonomy is an additional requirement for equality.

In particular the global propagation is RIGHT TO LEFT in the original
left-to-right box label b. If its rotated input is t_b and output
t'_b=U_b t_b, the actual original bottom ports are
(h(t'_b),h(t_b)^(-1)) and top ports are
(g(t'_b)^(-1),g(t_b)). Both original neighboring caps therefore
impose t_b=t'_(b+1); the outer turns impose t_s=t'_1. The condition
product U_b=1 closes this propagation in the order s,...,1. One must
not replace these literal relations by a forward box-label traversal.

The [audit](../experiments/audit_actual_pretzel_mixed_regular_character_lift.py)
checks the cleared rational identities, full two-by-two character and
threading formulas, complete parabolic limit, and the exact finite
source moment on both level parities. Finite computations supplement
the algebraic proof above.

## 6. Absolute complete crossing-circle holonomies match the geometric cusp

The [literal port and geometric-anchor proof](actual_pretzel_port_lift_and_geometric_anchor.md)
identifies the main meridians with the white-face holonomies of the
explicit four-antiprism construction. Here is an absolute matrix check
for the AUXILIARY generators; it is stronger than comparing cusp
Hessians or only a ratio of translations.

Set alpha=pi/s, c=cos(alpha), t=csc(alpha),

    rho^2=sec(alpha)+tan(alpha), R=rho^4,
    w=-R, U=exp(2i alpha),
    z_i=t rho^(-1) exp((2i+1)i alpha),

and use the actual raw port matrices

    g(z)=[[-2w/(w+1),z],[-t^2/z,-2/(w+1)]].

Their fixed flags are z/t. The unrotated disk product is

    P_i=g(z_i)g(Uz_i)^(-1),

with trace -2 and fixed flag Z_(i+1)=rho U^(i+1). Direct multiplication
gives

    (P_i)_21=t^2(1-t)(1-U^(-1))/z_i.

Rotate the boundary coordinate by zeta'=U^(-i-1)zeta and then use
m_i(zeta)=1/(zeta'-rho). The new lower-left entry before this last
Mobius map is

    c'=U^(i+1)(P_i)_21=2i rho(1-t).

For any trace-minus-two matrix fixing rho, write P=-I+N. The kernel
of N is (rho,1), so N=c'[[rho,-rho^2],[1,-rho]]. Conjugating by
the matrix [[0,1],[1,-rho]] of m_i gives

    m_i P_i m_i^(-1)=-I+[[0,c'],[0,0]].

Consequently its PROJECTIVE translation is -c'. Since
rho^2(t-1)=ct and the actual cusp rectangle has width
W=1/(rho sin(alpha))=t/rho, this translation is exactly

    -c'=2ic W.                                      (15)

The source-selected complete Y equals exp(2i atan(sec(alpha))), hence

    1+Y=2ic/(1+ic).

Using (12), the same coordinate m_i sends the actual auxiliary
meridian to the translation

    -c'/(1+Y)=(1+ic)W.                              (16)

Equations (15)--(16) are precisely the primitive disk longitude and
the POSITIVE diagonal half-twist meridian in
[the face-labeled cusp calculation](actual_augmented_pretzel_crossing_circle_cusp.md).
Thus the complete auxiliary matrices, not just their flags or their
first deformation derivative, match those of the actual half-twisted
augmented geometry. The central minus sign of the SL2 disk product
is retained throughout. Together with the independently checked white
and shaded face pairings in the port proof, this anchors the actual
complete representation, not merely its numerical volume.

Reversing the cyclic TRAVERSAL label to respect that operator order
does not change the oriented complete geometry. There is an explicit
holomorphic Mobius isometry F(zeta)=rho^2/zeta. It sends

    Z_k -> Z_(-k),
    U_k^+ -> U_(-k-1)^-, U_k^- -> U_(-k-1)^+,
    Q_k -> Q_(-k-1), T_k^+ <-> T_(-k)^-, W_+ <-> W_-.

Under the literal cross-copy shaded gluing, applying F to both sides
gives the SAME gluing at index -k read in its inverse direction:
the original U_(k-1)^+ -> U_k^- becomes
U_(-k)^- -> U_(-k-1)^+, and the other outer vertex behaves likewise.
Thus the reverse traversal is matched
by an orientation-preserving isometry, not by an assumed mirror
identification. The original boxes and their source labels are not
permuted in the quantum formula.
