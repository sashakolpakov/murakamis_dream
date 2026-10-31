# The controlled Fourier gauge sends the geometric cut clock to a conormal shift

Research proof, 27 October 2026. The controlled source gauge has an
explicit quadratic kernel. It gives exact transformed head Ward
operators, hence an actual crossing/current Hamiltonian dictionary.
It also distinguishes two clocks which have identical-looking
coherent coordinate descriptions but are different actual insertions.
The difference survives the normalized source pairing. The relevant
first-normal coupling is computed from the whole clock, not inferred
from its reduced root representative.

The result does not yet send both actual framing-current equations
to the full sourced geometric period. It identifies the required
polarization/normal adapter and rules out a source-preserving
identification which simply equates the coupled position clock with
the old geometric cut clock.

## 1. Exact finite kernel and observables

Use the actual high-color basis and source of
[the cyclotomic wall construction](cyclotomic_diagonal_wall_current_source.md),
with r=N. Write R=0,...,N for the Frobenius block index, S=0,...,N-1
for the head index, A=Q_N^S and B=Q_N^R. Let V increase S modulo N.
Take the explicitly normalized Fourier matrix

\[
 {\mathcal{F}}_{S',S}=N^{-1}Q_N^{S'S},\quad
 {\mathcal{F}}^{-1}_{S,S'}=Q_N^{-SS'},\quad
 H_0=G(I\otimes{\mathcal{F}}),\quad
 G=\sum_R P_R\otimes V^R.
\]

The actual matrix kernel is exactly

\[
 (H_0)_{R,S';R,S}=N^{-1}Q_N^{S(S'-R)}.             \tag{1}
\]

The reduction of S'-R modulo N changes no power of Q_N. Finite
geometric-series multiplication gives

\[
 \begin{split}
 H_0 A H_0^{-1}&=V^{-1},&
 H_0 V H_0^{-1}&=B^{-1}A,\\
 H_0 B H_0^{-1}&=B,&
 H_0e_{\mathrm{Fr}}H_0^{-1}&=e_{\mathrm{Fr}}V^{-1},&
 H_0f_{\mathrm{Fr}}H_0^{-1}&=f_{\mathrm{Fr}}V.
 \end{split}                                                   \tag{2}
\]

The Fr matrices in (2) are the actual divided matrices with their
root sign normalization, not an independent classical copy. Their
last two conjugates are exactly the endpoint-completed generators
constructed from divided powers and actual normal wrap entries.

In particular the OLD head clock is the NEW head shift. The new
position clock restricted to the correlated source satisfies
A|P=B|P, but this inserted A is not H_0 A_old H_0^(-1).
Conjugating an entire word transforms its old observables as well
as its sources; it does not replace this distinction by a choice
of terminology.

## 2. Actual transformed Ward operators, including the endpoints

First keep the original INTEGRAL head frame of the wall source.
Let M^2=1 and x=-M/q_N. The sign M is the retained meridian lift;
in the high r=N color it is (-1)^N before its specified
one-dimensional lift adapter. The genuine Hopf scaling is
Ecal=rho^2 E. With C_q=diag(q_N^S), the actual root matrices are

\[
 K=xA^{-1},\quad
 {\mathcal{E}}=M\rho V^{-1}(C_q-C_q^{-1}),\quad
 F=V(q_NC_q-q_N^{-1}C_q^{-1})/\rho.                 \tag{3}
\]

These are Ecal=M rho^2 E_St and F=F_St. Their E edge at S=0
and F edge at S=N-1 vanish exactly, since [0]=[N]=0.
Define the whole finite polynomial matrix

\[
 \Psi_w(V)=\frac1N\sum_{\ell=0}^{N-1}
                  \sum_{s=0}^{N-1}(wQ_N^\ell)^sV^\ell,
 \qquad\Psi_\pm=\Psi_{q_N^{\pm1}}.                 \tag{3a}
\]

It is exactly Fourier w^S Fourier^(-1). The controlled shift
commutes with this circulant matrix, so H_0 C_q^(+/-1)H_0^(-1)
=Psi_(+/-). Hence the exact transformed actual current operators,
in the SAME wall source frame, are

\[
 \begin{split}
 K^{H_0}&=xV,\\
 {\mathcal{E}}^{H_0}&=M\rho BA^{-1}(\Psi_+-\Psi_-),\\
 F^{H_0}&=B^{-1}A(q_N\Psi_+-q_N^{-1}\Psi_-)/\rho.
 \end{split}                                                   \tag{4}
\]

These are original head Ward currents for the ACTUAL conjugated
crossing: conjugate the input/output coproducts with the same
endpoint H_0's. The original exact R intertwining equation then
gives its exact transformed equation, with no omitted Cartan,
twist, cap, source or internal projector. Thus (4) is a concrete
crossing/current identity, not only an identification of orbit
dimensions or groups.

It has a useful negative consequence. The transformed Fr generators
in (2) commute with all three transformed head operators (4),
because the two original factors commute. They are distinct
commuting actions at the root. Calling the Fr generators the old
geometric head currents without a normal comparison would
contradict this exact operator fact.

For comparison there is a simpler BALANCED-frame formula, but its
frame adapter must not be erased. The explicit integral-to-balanced
diagonal matrix is

\[
 D_s=(1-Q_N)^s q_N^{s(s-1)/2}.
\]

Direct adjacent entries give D F_St D^(-1)=V(1-Q_NA) and
D(M rho^2 E_St)D^(-1)=V^(-1)(MA^(-1)-M^(-1)).
If one defines a FRESH unit shift and unit Fourier gauge H_B in
those balanced coordinates, its formulas are

\[
 {\mathcal{E}}^{H_B}=BA^{-1}(MV-M^{-1}),\quad
 F^{H_B}=B^{-1}A(1-Q_NV^{-1}),\quad K^{H_B}=xV.       \tag{4a}
\]

The transported original integral shift is instead D V D^(-1),
which is weighted. Thus H_B is not obtained by silently retaining
the same unit V while calling it the transported wall H_0. To
compare the two actual words one must include D (and its actual
whole q-germ when normal jets are compared), with both sources,
duals and every internal projector. The logarithm of this diagonal
can contribute to the phase. No Gaussian/large-level phase estimate
is inferred merely from its invertibility at fixed N.

The actual whole source gauge H(q)=K_src(q)H_0 of the wall note has
K_src(q_N)=I and retains its compression unit. Equation (4) is its
root dictionary. If K_src=I+delta K_src,1+O(delta^2), every first-normal
transformed operator has the additional term [K_src,1,O^(H_0)]. That known source-germ
term must be included rather than treating constant H_0 as the
entire whole source comparison.

## 3. The exact quadratic generating family and its conormal

Put H_N=2pi i/N and mark logarithmic positions

\[
 Q_R=H_NR,\quad q=H_NS,\quad q'=H_NS'.
\]

The kernel (1) is N^(-1) exp(W/H_N), with the exact quadratic
generating function

\[
                   W=q(q'-Q_R).                    \tag{5}
\]

Use dW=p'_h dq'+(p'_R-p_R)dQ_R-p_h dq. The canonical transformation
is therefore

\[
 Q'_R=Q_R,\quad q'=Q_R-p_h,\quad
 p'_h=q,\quad p'_R=p_R-q.                          \tag{6}
\]

It preserves dQ_R wedge dp_R+dq wedge dp_h. Logarithmic marks
are required: a cyclic index wrap adds its specified integral
2pi i period to the quadratic generator. It is not discarded
while composing marked phases. The root Frobenius parity remains
its separately recorded character.

The Fr index R is UNWRAPPED: R=0 and R=N are distinct endpoint
states even though B has the same eigenvalue there. No cyclic Fr
wrap is added to its nilpotent divided matrices. Formula (6) is the
local marked canonical map of the exact quadratic kernel; the
finite endpoint constraints and the Fr O(N) source clutch remain
in the finite operator problem. No analytic stationary-phase
comparison or global flat Weyl quantization of that source line
has been assumed.

For a normally ordered original head observable h(A,V), (2) is
an exact finite difference Egorov formula. Its leading Hamiltonian
is the old Hamiltonian under

\[
                 q=p'_h,\qquad p_h=Q_R-q'.         \tag{7}
\]

For example IN THE BALANCED FRAME the principal Hamiltonians are
e^p(M e^(-q)-M^(-1)) and e^(-p)(1-e^q). Under (7) they give
precisely the principal symbols of (4a). In the original integral
frame the functions Psi_+/- in (4) are retained instead; converting
their marked phase requires the displayed diagonal adapter. The
quadratic Hamiltonian dictionary itself follows directly from the
actual finite Fourier kernel, without importing a general
semiclassical Egorov theorem or suppressing this basis change.

The original uniform head source has p_h=0. Its image is the
actual constraint q'=Q_R, exactly P from the wall construction.
The Fr source psi(t)=sum_R t^Rv_R has p_R=Log t, so its correlated
image has the conormal relation

\[
             p'_R+p'_h=\operatorname{Log}t.         \tag{8}
\]

Thus the actual OLD cut position A_old=e^q is e^(p'_h), or
t/e^(p'_R), on this marked conormal. It is not e^(Q_R).
Equation (8) is a concrete relative-Fr-momentum adapter, including
the source parameter. It is a relation on a source conormal,
not a replacement of two independent momentum operators by
ordinary functions before contraction.

## 4. The normalized source detects the clock distinction

For every pair of Fr source flags, e_D is supported on the selected
states z_j of the wall theorem. A head shift changes S while fixing
R. Hence

\[
                  PV^{-1}P=0,\qquad
             \operatorname{Tr}(e_DV^{-1})=0.        \tag{9}
\]

On the same source the other insertion has the exact, nonconstant
character

\[
 \operatorname{Tr}(e_D A)
       =\left(\frac{1+Q_Ntu}{1+tu}\right)^N,\qquad
 T=\frac{tu}{1+tu}.                                \tag{10}
\]

Equations (9)--(10) are actual finite matrix pairings. Thus there
cannot be a source-preserving whole-observable comparison which
identifies these two clocks. The polynomial Fr-clock normal graph
in the parent's finite-clock construction is an actual INSERTED
clock image and a useful source cycle; it is not yet the image of
the old cut observable under (1). An additional polarization and
current comparison is necessary.

The same distinction appears in the original geometric directions.
In the old complete critical frame, both cut-Borel generators obey

\[
 \delta p_h=0,\qquad
 \delta q=-2(1-A_{\mathrm{old}}).                         \tag{11}
\]

Here delta p_h=0 is exactly ker(ell), the fixed inverse-cut-flag
condition, rather than a new gauge assumption. Lift these old
geometric directions without changing the ancillary Fr variables.
Equation (6) carries their CUT components to

\[
 \delta q'=\delta Q_R=0,\quad
 \delta p'_h=-2(1-A_{\mathrm{old}}),\quad
 \delta p'_R=2(1-A_{\mathrm{old}}).                       \tag{12}
\]

They lie in the relative conormal direction (8). Their independence
as the two full geometric framing fields is carried by the other
actual flow coordinates; it is invisible in these identical cut
components. One source clock or one cut current does not determine
that independent internal coordinate.

## 5. The whole clock has an exact first-normal Fr coupling

The normal coupling does exist, but it uses more data than a root
clock value. Before specializing let Q=q^2, Z=Q^N,
delta=1-Z, and retain the actual unwrapped color clock

\[
               C_Q=Q^{J_{\mathrm{un}}}=Q^S Z^R.         \tag{13}
\]

Let e(q)=tau E^(N)(q) and f(q)=F^(N)(q) be the actual generic
integral divided matrices; the sign tau is constant on the marked
root. They lower and raise R by one, respectively, while preserving
S. Thus matrix grading alone proves the exact whole identities

\[
 [e(q),C_Q]=(Z-1)C_Qe(q),\qquad
 [f(q),C_Q]=(Z^{-1}-1)C_Qf(q).                      \tag{14}
\]

Regular division and the root evaluation give the actual normal
cut-current insertions

\[
 [\,[e,C_Q]/\delta\,]_0=-A e_0,\qquad
 [\,[f,C_Q]/\delta\,]_0=A f_0.                      \tag{15}
\]

The same identities hold for the true tensor divided coproduct and
the TOTAL clock: every mixed coproduct term lowers or raises the
unwrapped total index by N. Hence (14)--(15) retain those mixed
terms, rather than replacing a divided Hopf action by a primitive
single-factor commutator. Actual R intertwining and total-index
conservation transport this normal identity through every crossing;
closing strands still requires its actual pivotal and relative
co-source rows.

### The full head resolvent in the correct polarization

The whole transformed clock can itself be written explicitly.
Write zeta=Q_N while Q remains the variable in the original
q-family, and keep H_0 fixed at zeta. Equation (3a) gives

\[
 C_Q^{H_0}=Z^R\Psi_Q(V),\qquad
 \Psi_Q(V)=\sum_{\ell=0}^{N-1}
       \frac{1-Q^N}{N(1-Q\zeta^\ell)}V^\ell.         \tag{15a}
\]

Every quotient in (15a) is the polynomial
N^(-1) sum_(s=0)^(N-1)(Q zeta^ell)^s. In particular its resonant
0/0 at ell=N-1 is not separately evaluated or removed. This
identity follows from the exact finite Fourier sum; it retains
the entire whole function before restricting its normal jets.

Its first normal is

\[
 \begin{split}
 C_Q^{H_0}=V^{-1}+\delta\bigg[
  -RV^{-1}-\frac{N-1}{2N}V^{-1}
  +\sum_{\ell\ne N-1}\frac{V^\ell}{N(1-\zeta^{\ell+1})}
                                  \bigg]+O(\delta^2).
 \end{split}                                                   \tag{15b}
\]

Thus the needed head pseudoinverse coefficients arise from the
actual Fourier-clock operator; they are not guessed to make two
classical vector fields agree. Equivalently the head part is
-V^(-1) Shat/N, where Shat=Fourier S Fourier^(-1). Its operator
norm is (N-1)/N in the root unit metric, since Fourier has condition
number one. The individual nonresonant coefficients and their
resonant diagonal term must be kept together.

Let e_t(q)=H_0 e(q)H_0^(-1), f_t(q)=H_0 f(q)H_0^(-1).
Their root values are the compensated generators e_Fr V^(-1)
and f_Fr V. They commute with the reduced whole head function
Psi_Q(V) for ALL q, because e(q),f(q) preserve S. Consequently
the head terms in their differentiated commutator cancel exactly.
The extra R term of (15b) alone supplies the remaining normal
interaction:

\[
 [e_t(0),-RV^{-1}]=-e_{\mathrm{Fr}}V^{-2},\qquad
 [f_t(0),-RV^{-1}]=f_{\mathrm{Fr}}.                      \tag{15c}
\]

These are precisely -C_0 e_t(0) and C_0 f_t(0) from (15), with
C_0=V^(-1). This is an explicit actual normal crossing/current
Hamiltonian identity in the CORRECT shift polarization. It shows
where the head resolvents cancel and where the surviving Fr normal
current originates, rather than identifying it from orbit names.

The whole source gauge does not invalidate the calculation. If
K_src=I+delta K_1+..., it adds [K_1,C_0] and [K_1,e_t(0)] to
the two first coefficients. Their extra commutator contributions
sum to [K_1,[e_t(0),C_0]]=0 by Jacobi; similarly for f. Thus the
normal coupling is preserved with the actual compression unit and
source germ retained. Nothing here removes the finite endpoint
or relative normal co-source when the word is closed.

### A nonzero actual old-clock normal map to the unprojectivized source line

Keeping the source line, rather than only its normalized projector,
provides a concrete additional comparison. Let r=N. On each actual
residue string use the homogeneous divided source

\[
 \psi_s(q;a,b)=a^N\exp((b/a)F^{(N)}(q))w_{0,s},\quad
 U_s(q;a,b)=\Lambda_s(q)\psi_s(q;a,b),               \tag{15d}
\]

where Lambda_s is the original actual divided co-source. The first
formula extends polynomially at a=0, since the terminating degree-R
term is a^(N-R)b^R(F^(N))^R/R!. At the root

\[
                U_s(q_N;a,b)=((a+b)/2)^N=:U_*.
\]

On a+b!=0 the U_s are units as whole q-germs. Keep the exact
root-one ratios and define the actual source/co-source

\[
 \psi=\sum_s\psi_s,\qquad
 \Lambda=\frac1N\sum_s\frac{U_0}{U_s}\Lambda_s,
 \qquad\Lambda\psi=U_0.                            \tag{15e}
\]

This is the whole retraction with a COMMON UNNORMALIZED source
line. Normalizing by U_0 returns the original scalar high-color
period; retaining it records the actual weight-N scale character.
The ratios U_0/U_s, with all their normal derivatives, have not
been set equal to their root value one.

For the actual old whole clock (13), finite matrix multiplication
gives the exact whole formula

\[
 \Lambda C_Q\psi
  =\frac{U_0(q;a,b)}N\sum_{s=0}^{N-1}Q^s
       \frac{U_s(q;a,bZ)}{U_s(q;a,b)}.              \tag{15f}
\]

Its root value is zero, but its regular normal quotient is

\[
 \boxed{\left[\frac{\Lambda C_Q\psi}{1-Q^N}\right]_{q_N}
       =\frac{((a+b)/2)^N}{N(1-Q_N)}.}              \tag{15g}
\]

Here is a proof retaining the source derivatives. Put D_Q=Q d/dQ.
The derivative of the ratio in (15f) is, at the root,
N mu with mu=b partial_b log U_*=Nb/(a+b), independent of s.
The explicit q-derivatives of the two U_s cancel in the ratio;
they were not assumed zero. This Fr mean term and the derivative
of U_0 multiply sum_s Q_N^s=0. The remaining head term is

\[
 \left.D_Q(\Lambda C_Q\psi)\right|_0
 =\frac{U_*}N\sum_s sQ_N^s=\frac{U_*}{Q_N-1},
 \qquad D_Q(1-Q^N)|_0=-N,
\]

which proves (15g) by regular division at the simple normal zero.
The entire expression (15f), not independent Taylor choices at
each string, specifies the lift being divided.

Thus the known head unit N(1-Q_N) extracts the actual source
character U_* from a literal OLD-cut-clock normal co-source.
Its inverse has uniformly bounded modulus:
1/(2pi)<=|1/[N(1-Q_N)]|<=1/4. No exponential adapter is hidden
in this factor. For an actual scalar long-knot matrix the same
calculation gives U_* K_N/[N(1-Q_N)] at the root, with the
original external peripheral line separately retained.

There is an exact root Borel-character statement as well. The
actual divided source is the degree-N coherent vector of (a,b),
and its fixed root row is the N-th symmetric power of (1,1)/2.
If (1,1)g=chi(g)(1,1), then U_*(g(a,b))=chi(g)^N U_*(a,b).
Equation (15g) is a nonzero equivariant map to this weight-N
source line. At the equal-flag anchor the generator e+f, which
fixes the normalized projector, acts on the unnormalized source
with weight N. That previously invisible scale has therefore
been retained by an ACTUAL clock-normal map, rather than inserted
after identifying two abstract Borel groups.

This is a map of the cut/normal source CHARACTER. It does not
equate the old clock value with a function of a+b, identify its
two full internal framing currents, or prove a geometric summand
survives the original finite cut. Dividing by U_0 at the outset
would discard exactly the scale which (15g) detects.
At this SELECTED SCALAR order the reduced clock Q^S gives the same
answer: its omitted Fr-mean term already vanishes in the root head
sum. Thus (15g) alone does not distinguish the whole and reduced
normal actions. Their distinction is the operator/current identity
(14)--(15), not an inferred independent scalar Fr current.

By contrast e(q) and f(q) commute with the reduced clock Q^S for
ALL q. Consequently (15) depends on the chosen whole lift (13).
Two observables with the same numerical root value give different
normal currents. This is exactly the whole-variable datum needed
before quantum jets are restricted.

There is also a precise limitation. The operation delta^(-1)ad(e)
is not a regular derivation of the entire Fr source algebra:
[e_0,f_0]=h_0 is generally nonzero. On delta times a lifted matrix
g its root value is [e_0,g_0], not zero. It therefore does not
descend to the root quotient independently of the lift. Equations
(14)--(15) define a normal/source-complex insertion with a specified
whole clock, not an ordinary classical vector field on every root
observable. The normal connection, source unit, and endpoints are
essential to extending it.

## 6. What the current dictionary now requires

The actual old head Hamiltonians and fields are explicitly given
by (4), (7), and (12), while (14)--(15) are an actual Fr-normal
coupling with every tensor mixed term retained. These are the two
concrete inputs to the missing framing-current comparison. Simply
mapping the Fr coherent quadric to the physical meridian graph
does not intertwine them, as (9)--(10) proves at the selected source.

In particular the bare Fr commutator fields cannot be substituted
for the two cut-Borel fields while preserving a clock A=e^(cT).
In x=Log v,T coordinates their actual coherent values are

\[
 X_e=v\partial_x+v(1-T)\partial_T,\quad
 X_f=-v^{-1}\partial_x-Tv^{-1}\partial_T,\quad
 X_h=2\partial_x.
\]

A fixed linear combination has T velocity
alpha v(1-T)-beta T/v. This can be a function of T alone only if
alpha=beta=0, whereas (11) requires a nonzero such function.
Head/source-dependent coefficients and the normal lift are
therefore necessary. Their existence as rational or logarithmic
functions is not itself the missing network-current identity.

No claim is made that this dictionary already kills the two full
Green boundaries or produces a nonzero full geometric period. It
specifies which physical observable, normal insertion and relative
conormal class the required map must preserve.

[Exact finite and symbolic audit](../experiments/audit_controlled_fourier_current_dictionary.py).
The tests concern the actual matrix/current identities and the
quadratic canonical map, not global cycle selection or asymptotics.
The [saved results](../experiments/controlled_fourier_current_dictionary_results.json)
pass seven full finite gauges N=2,...,8, both marked complete
meridian lifts, three Fr flag pairs, five actual normal families
N=2,...,6, and 323 nonzero mixed divided-coproduct entries.
Twenty actual divided-source cone checks include both polynomial
endpoints a=0 or b=0. Thirty nonconstant head-dependent source
normal units are retained in those tests; they have not been
replaced by constant binomial coefficients before checking (15g).
