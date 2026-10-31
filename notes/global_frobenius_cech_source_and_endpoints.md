# Global two-chart localization of the actual Frobenius source and its endpoints

Research construction, 27 October 2026. The actual high-color source
has an explicit global polynomial/Čech realization on P1. Its matrix
co-source is a Laurent cocycle, and the original matrix pairing is
exactly a residue. All actual whole matrices have global operator
lifts, unique up to an explicit cochain homotopy; their finite normal
jets admit the bounded-order lifts already proved. The two finite
source endpoints survive as named north and south cochains.

There is also a WHOLE rational comparison with the uniform co-source:
integrate the actual homogeneous dual WITH its retained pairing
weight, then normalize its actual pairing unit. A rational unipotent
gauge fixes the actual source and compares the two duals exactly.
No quantum-jet inference is needed for that identity.

This localizes the actual source/dual and operators globally. It
does not identify the network Gaussian coefficients with geometric
ones, bound the norm of endpoint transport, or prove the volume limit.

## 1. Actual polynomial source and an explicit dual Čech class

Fix N>=2 and use the actual Fr multiplicity basis v_k, 0<=k<=N,
of [the high integral color](high_integral_color_frobenius_wall_source.md).
Put

\[
       v_k\longmapsto {N\choose k}z^k.                \tag{1.1}
\]

The actual Fr module is thereby the global polynomial space of O(N).
On the two charts z and w=1/z, a section is a pair satisfying
f_infty(w)=w^N f_0(1/w). Thus e_infty=z^N e_0, and its global
sections are exactly the polynomials f_0 of degree at most N.
This verifies the global-section description directly from the
transition, with no cohomology theorem as a premise.

For the dual use e_0^* dz in the north and e_infty^* (-dw) in the
south. Its transition is +z^(-N-2). The Čech complex is

\[
 C^0=k[z]\oplus k[w]\ \xrightarrow{\ d\ }\
 C^1=k[z,z^{-1}],\qquad
 d(a_0,a_\infty)=z^{-N-2}a_\infty(1/z)-a_0(z).       \tag{1.2}
\]

The sign in -dw is deliberate. It retains both the canonical-bundle
degree -2 and the orientation of the residue below. Its cokernel
has the literal basis z^(-1),...,z^(-N-1); its kernel is zero.
The actual row co-source lambda is represented by

\[
 c_\lambda(z)=\sum_{k=0}^{N}
              \frac{\lambda(v_k)}{\binom Nk}z^{-k-1}. \tag{1.3}
\]

The pairing is EXACTLY the original matrix pairing:

\[
                   \lambda(\psi)=
      \operatorname{Res}_{z=0}c_\lambda(z)f_\psi(z)\,dz. \tag{1.4}
\]

Both kinds of coboundary in (1.2) pair to zero with a degree-N
global section: the north term is polynomial, while the south
term has powers at most -2 after multiplication. Conversely the
N+1 coefficients in (1.3) detect every polynomial coefficient.
This proves the perfect pairing directly, including its two-chart
quotient, rather than citing Serre duality as a proof.

The literal normalized matrix TRACE is preserved too, without
replacing it by a rank-one row:

\[
 \frac{\operatorname{Tr}D}{N+1}
  =\frac1{N+1}\sum_{k=0}^N\operatorname{Res}_{z=0}
       \frac{z^{-k-1}}{\binom Nk}
                    D\left(\binom Nk z^k\right)dz.    \tag{1.5}
\]

This works for arbitrary inserted matrices, not only diagonal
closed knot matrices. Source/co-source rows and the trace are
distinct retained pairings in this model.

## 2. The cochain projection and its explicit endpoint homotopy

Let pi retain exactly powers -1 through -N-1 and interpret them
by (1.3). Let iota take the canonical representative (1.3). For
a Laurent polynomial c write c=c_north+c_mid+c_south, with powers
respectively >=0, -N-1 through -1, and <=-N-2. Define

\[
 h(c)=\left(-c_{\mathrm{north}}(z),\
                   [z^{N+2}c_{\mathrm{south}}(z)]_{z=1/w}\right).
                                                               \tag{2.1}
\]

Then, coefficient by coefficient,

\[
 d h=I-\iota\pi\quad\text{on }C^1,\qquad
 h d=I\quad\text{on }C^0.                            \tag{2.2}
\]

These formulas explicitly contract the redundant Čech terms; no
endpoint is declared zero without its cochain.

For comparison the source complex of O(N) has differential
d_S(f_0,f_infty)=z^N f_infty(1/z)-f_0. Its global projection is
pi_S(f_0,f_infty)=[f_0]_(0..N), and a right inverse of d_S is

\[
 h_S(b)=\left(-b_{>N}(z),\
                         [z^{-N}b_{\le N}(z)]_{z=1/w}\right).
                                                               \tag{2.3}
\]

Direct substitution gives d_S h_S=I and
h_S d_S=I-iota_S pi_S. These are global chain maps and homotopies
over the chosen coefficient algebra.

There is even a cochain-level residue Stokes identity. Pair a source
0-cochain f with a dual 1-cochain c by Res(f_0 c dz), and a source
1-cochain b with a dual 0-cochain a by
Res(b z^(-N-2) a_infty(1/z) dz). Then

\[
                    \langle d_Sf,a\rangle
                         +\langle f,da\rangle=0.       \tag{2.4}
\]

The sum is the residue of
z^(-2) f_infty(1/z)a_infty(1/z)-f_0(z)a_0(z), which is zero.
Thus the source and dual endpoints are paired globally, not only
at one formal Taylor chart.

## 3. All actual whole operators lift, and finite jets have bounded order

In the polynomial model the original root divided generators are

\[
       e=\partial_z,\qquad f=Nz-z^2\partial_z,
       \qquad h=N-2z\partial_z.                       \tag{3.1}
\]

Reciprocal transport by f_infty(w)=w^N f_0(1/w) exchanges e and f
and changes h to -h. Hence they are global differential operators
on O(N), with their actual zero-order N terms retained.

Every actual WHOLE Fr matrix, not just a jet, has an explicit such
lift. Put A=z partial_z and
\(P_j(A)=\prod_{l\ne j}(A-l)/(j-l)\), 0<=j<=N. Matrix units are

\[
 E_{ij}=\begin{cases}
 (j!/i!) f^{i-j}P_j(A),&i\ge j,\\
 ((N-j)!/(N-i)!) e^{j-i}P_j(A),&i<j.
 \end{cases}                                                    \tag{3.2}
\]

They act literally as E_ij on the actual basis (1.1). Thus an actual
whole high-color crossing or Green matrix, with arbitrary head
coefficients, gives global operators on the product of the Fr
projective lines. Formula (3.2) may have order growing with N;
it is a whole-function lift, not a uniform-order assertion.
At quantum-normal depth B the actual
[all-order Fr theorem](high_color_all_normal_frobenius_filtration.md)
gives the much smaller differential-order bound 2B. Heads are
ordinary matrix coefficients throughout.

For D=sum a_l(z)partial_z^l, the dual lift is the formal adjoint

\[
                  D^\dagger c=
                        \sum_l(-\partial_z)^l(ca_l).  \tag{3.3}
\]

Residues of Laurent derivatives are zero, so (3.3) is the EXACT
row action lambda -> lambda D under (1.4). With head-matrix
coefficients this ordering is essential: the co-source row is
multiplied by a_l before differentiating, or equivalently its
dual column uses the transpose matrices. In particular

\[
 e^\dagger=-\partial_z,\quad
 f^\dagger=z^2\partial_z+(N+2)z,\quad
 h^\dagger=2z\partial_z+N+2.                           \tag{3.4}
\]

The +2 is the canonical-bundle contribution, not an adjustable
normalization. These maps preserve north and south coboundaries.
At infinity they exchange e^dagger and f^dagger and change h^dagger
to its negative, exactly as their source counterparts do. Thus they
are strict chain maps on (1.2).

If two global operator expressions induce the SAME actual matrix,
their dual lifts differ by an explicit null homotopy. More generally
for any lift D^dagger with induced actual dual matrix D^*,

\[
 D^\dagger-\iota D^*\pi
                =d(hD^\dagger)+(hD^\dagger)d.         \tag{3.5}
\]

On C^1 this is (2.2), because pi D^dagger=D^* pi; on C^0 use
commutation with d and h d=I. Thus the construction is a canonical
global action UP TO THESE SPECIFIED HOMOTOPIES. It is not a falsely
strict embedding of the full finite matrix algebra into a domain
of scalar differential functions. Composition and tensor products
carry the corresponding homotopies. On source global sections and
dual cohomology, all original matrix identities are literal.
For the source complex the analogous explicit homotopy is
H=h_S D+(iota_S pi_S)D h_S: it identifies D with
iota_S D_matrix pi_S. Its extra term is needed because the chosen
north coefficient projection need not commute with D on noncycles.

All formulas are linear over the actual whole coefficient ring.
The original q^N, M^N, half-root phases and source normalization
units stay as coefficients before restriction. A base shift or
derivation acts on those coefficients with its original Leibniz
law. One may restrict to finite quantum jets AFTER these whole
identities; there is no replacement of actual dual coefficients
by their root values before differentiation.
Explicitly, for a supplied base automorphism sigma and transport
T=C sigma, the dual row transport is sigma^(-1)(lambda C), with
pairing sigma^(-1)<lambda,Tv>. A supplied connection D_x+Omega
has dual D_x lambda-lambda Omega. These original semilinear and
connection rules commute with the coefficientwise Čech contractions;
the construction does not replace them by a root-only scalar action.

## 4. Whole clock automorphisms retain their line factors

For the actual clock B_xi=xi^A the north source action is
f_0(z)->f_0(xi z). Its southern action is

\[
                     f_\infty(w)\longmapsto
                                \xi^N f_\infty(w/\xi).\tag{4.1}
\]

The dual north and south actions are respectively

\[
 c(z)\longmapsto\xi^{-1}c(z/\xi),\qquad
 a_\infty(w)\longmapsto\xi^{N+1}a_\infty(\xi w).      \tag{4.2}
\]

They commute with the Čech differential and are ADJOINT for the
residue pairing: <B_xi^dagger c,f>=<c,B_xi f>. Simultaneously
transporting a source and its dual instead uses the contragredient
inverse: c(z)->xi c(xi z), and
a_infty(w)->xi^(-N-1)a_infty(w/xi). On z^(-k-1), (4.2)
multiplies by xi^k, exactly the actual
row clock. Its infinitesimal adjoint is -z partial_z-1; the -1
must not be dropped. These are the global line factors behind
the finite coherent dilations, including controlled clock gauges.

## 5. Literal north and south finite-source endpoints

The actual partial inverses are
e^+v_j=v_(j+1)/(N-j) for j<N and zero at N, and
f^+v_j=v_(j-1)/j for j>0 and zero at zero. In polynomials, e^+ is
the primitive anchored at z=0, with its degree-(N+1) tail removed.
The operator f^+ is the reciprocal south primitive. Directly,

\[
 e^+e=I-P_0,\quad ee^+=I-P_N,\qquad
 f^+f=I-P_N,\quad ff^+=I-P_0.                          \tag{5.1}
\]

They also have explicit global differential lifts. Let q(A) be the
degree-at-most-N interpolation polynomial with
q(j)=1/[(j+1)(N-j)] for j<N and q(N)=0. Then

\[
                         e^+=f q(A),\qquad
                         f^+=e q(N-A).               \tag{5.2}
\]

Their order can grow with N. Do NOT apply the bound 2B to these
arbitrary anchored primitives without their actual degree analysis.
Identities (5.1) hold strictly on H0; for the global Čech lifts their
differences are the explicit homotopies (3.5), with the endpoint
projectors retained.

The dual endpoint cochains are especially transparent:

\[
 \begin{split}
 f^\dagger z^{-1}&=N+1=d(-(N+1),0),\\
 e^\dagger z^{-N-1}&=(N+1)z^{-N-2}=d(0,N+1).
 \end{split}                                                    \tag{5.3}
\]

They are NORTH and SOUTH boundaries separately. Removing both
before pairing a relative source would erase its endpoint data.
The [actual endpoint-completed clock current](endpoint_completed_normal_clock_euler_current.md)
uses precisely these complementary finite primitives to restore
its missing endpoint. No Hopf-natural tensor inverse is asserted.

## 6. The actual paired Borel source is a global residue class

For the [marked unprojectivized source](actual_unprojectivized_frobenius_borel_torsor.md),
use U=alpha^N and m=(1-u)/(1+u). Its ROOT representatives are

\[
 \begin{split}
 f_\alpha(z)&=U(1+z)^N,\\
 c_{U,m}(z)&=\frac1{2^NU}\sum_{k=0}^N
                  (1-m)^k(1+m)^{N-k}z^{-k-1}.
 \end{split}                                                    \tag{6.1}
\]

They are globally polynomial in m, including the missing u=infinity
chart, and Res(c f dz)=1. The scale and descendant are residues
of ACTUAL operators:

\[
 U=\operatorname{Res}c_+f_\alpha dz,\quad
 m=\frac1N\operatorname{Res}c_{U,m}(N-2z\partial_z)f_\alpha dz,
 \qquad c_+=2^{-N}\sum_{k=0}^Nz^{-k-1}.               \tag{6.2}
\]

Consequently the already proved framing identity
Omega_cut=(A/N)dlogU wedge dm is an explicit expression in global
source/descendant residue pairings, on its marked Kummer cover.
The Berry form is still N dlogalpha and flat on this Borel;
it has not been substituted for Omega_cut.

There is an explicit relative framing coordinate too. On the same
marked cover put s=C alpha^2,
r_frame=(1+m)/2+D alpha^2, and

\[
       \tau=r_{\mathrm{frame}}/s
             =\frac{1+m}{2C\alpha^2}+\frac DC,
       \quad A=1/(1+s),\qquad
                 d\tau\wedge d\log A=\Omega_{\mathrm{cut}}.\tag{6.3}
\]

At C=alpha=1,D=0, one has s=1,A=1/2 and tau=(1+m)/2.
Thus the literal framing interval 0<=tau<=1 is m in [-1,1],
with d tau=dm/2. Averaging its ROOT global class c_(1,m) gives
the uniform row class

\[
       c_{\mathrm{uni}}(z)=\frac1{N+1}\sum_{k=0}^N
                            \frac{z^{-k-1}}{\binom Nk}.\tag{6.4}
\]

The whole extension of this relative identity is Section 7, with
its original pairing density retained.

The actual first-normal old cut clock also has a global class here.
Its previously proved value on every pure-power source is
((a+b)/2)^N/[N(1-Q_N)]. Since those source vectors span the actual
Fr module, the unique linear extension of this SELECTED coherent-family
character is represented by
c_+(z)/[N(1-Q_N)]. Pairing it with f_alpha returns U/[N(1-Q_N)].
This localizes the actual SCALE normal class globally; it neither
equates the framing A with an old clock nor supplies a second
internal geometric-current map.
The original normal construction has source-dependent pairing-unit
ratios. No equality of its full operator action on arbitrary Fr
matrices follows merely from this coherent-family character.

For the original whole q-source, use (1.3) on its actual coefficients
psi_s(q),lambda_s(q), including the actual units U_s(q,m). Formula
(6.1) is their root restriction, NOT their replacement before quantum
differentiation. Their whole source and dual remain global Čech data.

## 7. A whole retained-weight interval gives the uniform co-source

Here is a function identity before any normal-jet restriction.
Work over the actual rational q-coefficients near q_N on one
residue string. Put E_N(q)=tau E^(N)(q), F_N(q)=F^(N)(q), and

\[
 \begin{split}
 \psi_q&=\exp(F_N(q))v_0,\\
 c_k(q)v_k^*&=v_0^*E_N(q)^k/k!,\\
 \widetilde\lambda_q(m)&=\sum_{k=0}^N
       c_k(q)\left(\frac{1+m}{2}\right)^{N-k}
             \left(\frac{1-m}{2}\right)^k v_k^*,\\
 U_q(m)&=\widetilde\lambda_q(m)\psi_q,\qquad
 \lambda_q(m)=\widetilde\lambda_q(m)/U_q(m).
 \end{split}                                                    \tag{7.1}
\]

Every c_k and psi coefficient comes from the original integral
divided matrices. At the root c_k=binom(N,k), psi_q=sum v_k and
U_q(m)=1. Thus U is an actual pairing unit formally, and analytically
on the compact interval for q sufficiently close to q_N at fixed N.

The literal beta integral, proved by repeated elementary integration
of t^a(1-t)^b, is

\[
 \frac12\int_{-1}^1
       \left(\frac{1+m}{2}\right)^{N-k}
       \left(\frac{1-m}{2}\right)^kdm
                =\frac1{(N+1)\binom Nk}.             \tag{7.2}
\]

Therefore the WHOLE weighted interval co-source is rational:

\[
 L_q=\frac12\int_{-1}^1 U_q(m)\lambda_q(m)dm
      =\sum_k\frac{c_k(q)}{(N+1)\binom Nk}v_k^*.       \tag{7.3}
\]

Cancellation of U in (7.3) is an identity of the WHOLE rational
integrand, before integration or normal specialization. It retains
that pairing line as the integration density. At q_N the row is
the uniform row lambda_uni=(sum v_k^*)/(N+1).

This uniform ROW is distinct from the full trace (1.5). With its
uniform source it agrees with the trace on diagonal arrays, and
both give the actual closed scalar period. No equality on arbitrary
off-diagonal Green insertions is inferred from that fact.

Nor is the uniform Fr row the original head-uniform/coherent-Fr
coupon after the cyclotomic diagonal projector. Its Fr indices
0 and N both map to head index S=0, so raw Fr uniform averaging
counts that head endpoint twice. A literal match to the old head
co-source requires the degree-elevation/endpoint map or its retained
adapter. The root-original coherent Fr row has binomial weights;
it is a different co-source from lambda_uni. The root-identity gauge
below compares the WEIGHTED-INTERVAL Fr uniform dual with the Fr
uniform dual, not automatically with that binomial coupon.

Put V_q=L_q psi_q and nu_q=lambda_uni psi_q. Both are actual rational
units with root value ONE. The normalized retained-weight interval
is L_q/V_q. The normalized uniform dual on the SAME actual source
is lambda_uni/nu_q. Define

\[
 \Delta_q=L_q/V_q-\lambda_{\mathrm{uni}}/\nu_q,\qquad
                    K_q=I+\psi_q\Delta_q.            \tag{7.4}
\]

Since Delta_q psi_q=0, these are exact whole identities:

\[
 \begin{split}
 K_q^{-1}&=I-\psi_q\Delta_q,\quad K_{q_N}=I,\\
 K_q\psi_q&=\psi_q,\qquad
       (\lambda_{\mathrm{uni}}/\nu_q)K_q=L_q/V_q .
 \end{split}                                                    \tag{7.5}
\]

Thus (7.4) is a concrete regular RATIONAL unipotent source-preserving
gauge between the two whole co-sources. It is not an inference from
equality of their root jets. The marked scale alpha^N is retained
by multiplying psi and the dual inversely; K itself is unchanged.

To compare network operators one must conjugate them too. In the
convention v_old=K_q v_new, transport becomes
K_q^(-1)T_old sigma(K_q), co-source becomes ell_old K_q, and a
connection becomes K_q^(-1)Omega_old K_q+K_q^(-1)dK_q. Its last
term is part of the actual comparison. Formula (7.5) alone is not
a proof of geometric current intertwining. The chosen source gauge
is not declared PBW-degree-preserving, nor is its growing-N
presentation declared uniformly bounded.

The UNWEIGHTED normalized integral int lambda_q(m)dm/2 is a different
relative rational-function period, potentially logarithmic. No
rationality or equality to (7.3) is asserted. The source density
U_q(m)/V_q is essential off the root; setting it to one would lose
exact actual quantum-normal data.

## 8. Precise category and remaining geometric identification

At fixed N this construction works on whole algebraic source and
dual bundles over the actual rational coefficient ring, retaining
its marked units, phase and Kummer charts. Operators are global
differential operators and bundle automorphisms, with explicit
Čech lifts. Different lifts of the same actual matrix are identified
by the concrete cochain homotopies (2.2)--(3.5). Relative periods
retain their density and endpoints; unweighted periods need not
be rational sections. Quantum jets are restrictions of these
already specified whole identities.

Tensoring the displayed two-chart complexes handles all Fr strands
of an actual braid: source sections are multihomogeneous polynomials,
dual classes are products of the Laurent basis elements, and the
matrix pairing is their ordered multiple residue. The local strict
operator lifts compose; identities in finite matrices lift up the
explicit tensor contractions. Thus actual whole R/Green operators,
their source units and named finite endpoints have a GLOBAL source
model, not only a formal coordinate patch at the optimizer.

The further map to the INTERNAL geometric framing interval still
requires its actual Ward/current comparison, including the charged
head neighbors and normal source corrections. The
[actual relative endpoint analysis](actual_frobenius_relative_endpoint_period.md)
also shows that exact endpoint transport can have exponentially
large metric norm. Global algebraic localization and equality of
source pairings do not supply a tame norm or a nonzero selected
geometric contribution.

[Exact global source/Čech audit](../experiments/audit_global_frobenius_cech_source.py).
[Results](../experiments/global_frobenius_cech_source_results.json).
[Independent proof audit](high_color_wall_source_independent_audit.md).
