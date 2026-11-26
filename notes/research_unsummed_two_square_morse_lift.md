# The full wire–angle phase at a two-square fold

Private written proof, 16 November 2026.

The original stationary wire can cease to be a holomorphic function
of its endpoint angles when its square root vanishes. At the radial
limits classified in the pinned two-square theorem, this does not
make the full unsummed wire–angle phase degenerate. Its critical
equations are locally equivalent, by explicit holomorphic units, to
the regular lifted primitive system. The full holomorphic Hessian is
therefore nonsingular, including at every admitted \(q_e=0\).

This is a statement about the retained original phase and its local
holomorphic germ. It neither assigns its coefficient in the finite
source nor constructs a completed cone metric at the two-square
limit. The phase of a reversed-index kernel or of a genuinely free
cardinal boundary factor is not substituted by a same-index
factorial phase.

## 1. The original phase and its marked germ

Use the hypotheses and limiting data of
[the two-square primitive lift](research_radial_two_square_primitive_lift.md):
a finite connected original ordered circle tree, a nonempty proper
selected set \(S\), complete outside angles, fixed integer original
powers \(n_v=\eta_v-2p_v\), and a supplied positive unit-charge
solution. A sequence of actual positive common-charge solutions
has a finite corner limit at \(0<\chi_*<1\).

All limiting selected angles have
\[
 t_v=s_v-iH_v,\qquad H_v>0,\qquad |s_v|<\pi.
 \tag{1}
\]
Every included edge is positive, a regular single-square corner,
or a two-square matching edge whose endpoints each have another
positive edge. On a two-square edge
\[
 a=\tan(t_v/2)=-iA,\quad b=\tan(t_w/2)=-iB,\quad
 0<A,B<1,\quad q=iQ,\quad Q^2=A^2+B^2-1\ge0,
 \tag{2}
\]
so \(|Q|<\min(A,B)<1\). A fold has \(Q=0\).

For each original same-index edge retain its wire coordinate \(x_e\)
and the literal incidence phase
\[
 b_0(x,t)=-J(1/2-x+t/(2\pi))
          -J(1/2-x-t/(2\pi))-2J(x),\qquad
 J'(z)=\Log(2\sin\pi z).
 \tag{3}
\]
Here \(b_0\) denotes a phase, not the endpoint tangent \(b\).
The full charged phase is
\[
 \Phi_c(\mathbf x,\mathbf t)
   =\sum_{e=vw}\{b_0(x_e,t_v)+b_0(x_e,t_w)\}
       +\sum_{v\in S}
           \left(\frac{i n_vt_v^2}{4\pi}-ic_vt_v\right).
 \tag{4}
\]
Outside angles are fixed, so their derivatives are omitted.
The base charge is \(c_v=\chi_*\). No wire is eliminated in (4).

On the positive approach the original stationary wires satisfy
\[
 q_e=\cot(\pi x_e),\qquad q_e^2=1+a^2+b^2.
 \tag{5}
\]
The inverse through \(q=1,x=1/4\) is
\[
 x(q)=\frac{1}{2\pi i}\Log\frac{q+i}{q-i},\qquad
 \frac{dx}{dq}=-\frac1{\pi(1+q^2)}.
 \tag{6}
\]
For a positive or single-square edge, \(\Re q>0\) and
\(0<\Re x<1/2\). On a two-square edge its limit is
\[
             x(iQ)=\frac12-\frac{i}{\pi}\operatorname{artanh}Q.
 \tag{7}
\]
Thus \(x=1/2\) at a fold. In all cases \(q^2+1\ne0\), so
(6) is a local holomorphic coordinate change even at a fold.

Every sine appearing in (3) is nonzero at this stationary limit.
Indeed \(\sin\pi x\ne0\), and
\[
 \begin{aligned}
 \sin\pi(1/2-x+t/(2\pi))
    &=\sin\pi x\,\cos(t/2)(q+a),\\
 \sin\pi(1/2-x-t/(2\pi))
    &=\sin\pi x\,\cos(t/2)(q-a).
 \end{aligned}
 \tag{8}
\]
All factors on the right are units by (1)--(2) and the pinned
classification of the other edges.

Consequently the logarithmic derivatives in (3) extend to a small
simply connected neighborhood in the full independent variables
\((x_e,t_v)\). Their constants are those reached from the positive
approach. In particular the marked lift has
\[
 F_{e,x}=0,\qquad
 b_{0,t}(x_e,t_v)=-r_{v,e}/\pi
 \quad\hbox{at the stationary limit},\qquad
 F_e=b_0(x,t)+b_0(x,u).
 \tag{9}
\]
These are the original positive-source identities passed to the
limit, not logarithms reset from their exponentials. One can
equivalently determine the local germ by its holomorphic sine-log
derivatives and (9), with the critical constant continued from
the original phase.

There is no branch-existence assertion hidden here. The finite
sharp square limits have bounded strip coordinates, with limiting
disk points away from \(1,-1,i,-i\). A sufficiently small product
of disk neighborhoods meets the positive bidisk in a connected
simply connected set. On that set the unit factors in (8) and
their logarithms are the original ones. Their local extensions,
including at \(q=0\), give precisely the germs just specified.

## 2. Exact equivalence of the critical equations

Temporarily make \(q_e\) an independent variable for every edge,
using (6) to change the wire coordinates. Write
\[
 f_e=q_e^2-1-a^2-b^2,\qquad
 d_e=(1+a^2)(1+b^2),\qquad
 \gamma_e=\frac{1+q_e^2}{d_e}.
 \tag{10}
\]
These denominators are units near the limiting point. For the
holomorphic function germ
\[
                         L(z)=\frac{\Log(1+z)}z,\qquad L(0)=1,
 \tag{11}
\]
use its local branch at zero.

The exact exponentiated original wire equation is
\[
 \begin{aligned}
 \exp F_{e,x}
 &=\frac{(q_e^2-a^2)(q_e^2-b^2)}
          {(1+a^2)(1+b^2)}\\
 &=1+\gamma_e f_e.
 \end{aligned}
 \tag{12}
\]
For the first equality, differentiate (3), multiply the two
incidence sine ratios, and use \(\sin^2\pi x=1/(1+q^2)\).
For the second, expand the numerator difference:
\[
 (q^2-a^2)(q^2-b^2)-(1+a^2)(1+b^2)
                        =(1+q^2)(q^2-1-a^2-b^2).
 \tag{13}
\]
The zero lift in (9), retained in the local neighborhood, therefore
gives the unexponentiated identity
\[
 F_{e,x}=\gamma_e f_e L(\gamma_e f_e).
 \tag{14}
\]

Define the off-constraint original logarithmic extension by
\[
 \widehat r_{v,e}
       =\log\{\cos(t_w/2)(q_e+a)\},\qquad
 \widehat r_{w,e}
       =\log\{\cos(t_v/2)(q_e+b)\}.
 \tag{15}
\]
Its branches have the limiting original values. Set also
\[
 \widetilde r_{v,e}=\tfrac12\Log\frac{q_e+a}{q_e-a},
 \qquad b_{0,t}(x_e,t_v)=-\widetilde r_{v,e}/\pi,
 \tag{16}
\]
with the same continued lift. The elementary factor identity
\[
 \cos^2(t_w/2)(q_e+a)(q_e-a)
       =\frac{q_e^2-a^2}{1+b^2}
       =1+\frac{f_e}{1+b^2}
 \tag{17}
\]
proves
\[
 \widehat r_{v,e}-\widetilde r_{v,e}
       =\frac12\Log\left(1+\frac{f_e}{1+b^2}\right).
 \tag{18}
\]
There is no additional logarithmic constant: both sides vanish on
the continued stationary sheet. The analogous formula at \(w\)
interchanges \(a,b\).

Put
\[
 \widehat{\mathcal P}_v
   =\sum_{e\ni v}\widehat r_{v,e}-\frac{i n_vt_v}{2},
 \qquad
 G_v=\widehat{\mathcal P}_v+\pi i c_v.
 \tag{19}
\]
Let \(\widetilde\Phi_c(q,t)=\Phi_c(x(q),t)\). Its full gradient
obeys the exact local identities
\[
 \boxed{\begin{aligned}
 \partial_{q_e}\widetilde\Phi_c
      &=-\frac{L(\gamma_e f_e)}{\pi d_e}\,f_e,\\
 \partial_{t_v}\widetilde\Phi_c
      &=-\frac{G_v}{\pi}
        +\sum_{e=vw}
           \frac{L(f_e/(1+a_w^2))}
                {2\pi(1+a_w^2)}\,f_e .
 \end{aligned}}
 \tag{20}
\]
The angular derivative is taken with the independent \(q_e\)
fixed, equivalently with the corresponding \(x_e\) fixed.

In particular, if the equation vector is ordered as \((f,G)\),
then the full gradient is an invertible triangular holomorphic
matrix times that vector. Its first diagonal entries are
\(-L(\gamma_e f_e)/(\pi d_e)\); its selected angular diagonal is
\(-I/\pi\). Hence the two generated local holomorphic ideals are
equal:
\[
  \big\langle d\widetilde\Phi_c\big\rangle
             =\big\langle(f_e)_e,(G_v)_{v\in S}\big\rangle .
 \tag{21}
\]
This is a local identity for the exact continued phase, rather
than an analogy between two stationary equations.

## 3. Nonsingularity of the full Hessian

**Theorem.** At the supplied radial corner limit, the full
holomorphic Hessian of (4) in all retained wire variables and
selected angular variables is nonsingular. The conclusion includes
every fold edge \(q_e=0\).

**Proof.** First consider the Jacobian of \((f,G)\) in all
independent \((q,t)\). On a nonfold edge
\(\partial f_e/\partial q_e=2q_e\ne0\), so its constraint
can be solved for the original local square root. Eliminating
these constraints leaves exactly the lifted fold and primitive
system of the pinned two-square theorem. That system has
invertible Jacobian. The full constraint/primitive Jacobian is
therefore invertible as well.

At a critical point, differentiation of (20) multiplies this
Jacobian by the invertible triangular matrix in (21). Terms
differentiating that matrix vanish because \(f=G=0\). Thus
\(\operatorname{Hess}_{(q,t)}\widetilde\Phi_c\) is invertible.
The coordinate change (6) has invertible differential, and a
critical Hessian transforms by congruence. This proves the assertion
in the original \((x,t)\) coordinates. \(\square\)

For an explicit local check, the wire-only negative second
derivative is the familiar original expression
\[
 -F_{e,xx}=
       \frac{2\pi q_e(1+q_e^2)^2}{(1+a^2)(1+b^2)}
                 \quad\hbox{when }f_e=0.
 \tag{22}
\]
It vanishes at a fold. There, with the notation of (2) and
\(A^2+B^2=1\), the mixed wire–angle row is instead
\[
 F_{e,x(t_v,t_w)}
                      =\frac{i}{AB}(B,A)\ne0.
 \tag{23}
\]
Indeed \(df_e=iAB(B\,dt_v+A\,dt_w)\), and (14) at the fold
has coefficient \(1/(A^2B^2)\). The same vector is the real
constraint normal used in the lifted primitive proof. The positive
edges forced beside each two-square edge control the complementary
angle directions. This is why the joint system stays regular even
though the wire-only Hessian vanishes.

More precisely, with the ordering in (21) and
\(d=|E|+|S|\), at the critical point
\[
 \det\operatorname{Hess}_{(q,t)}\widetilde\Phi_c
       =\frac{(-1)^d}{\pi^d\prod_e d_e}
           \det D_{(q,t)}(f,G).
 \tag{24}
\]
Passing to \((x,t)\) multiplies this determinant by
\(\prod_e\{\pi(1+q_e^2)\}^2\), a nonzero factor.
No lower bound uniform over unspecified radial limits is inferred
from this local determinant identity.

The holomorphic Morse lemma consequently gives local coordinates
\(\xi_1,\ldots,\xi_d\), with nonzero Jacobian, in which
\[
             \Phi_c=\Phi_c(x_*,t_*)-\frac12\sum_{j=1}^d\xi_j^2.
 \tag{25}
\]
Real \(\xi\) give a strictly descending local real \(d\)-disk.
These coordinates generally mix wire and angle variables.
They do not assert concavity on the original horizontal product
contour. They also do not repair the singular operation of
eliminating the fold wire as a function of arbitrary endpoint
angles.

## 4. Relation to the exact factorial source

For \(N\ge2\), \(D=N-1\), the actual halfwire interpolation is
\[
 B_N(x,t)=\frac{N}{
 G_N(D/2-Nx+Nt/(2\pi))
 G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
 \tag{26}
\]
The exact divisor result used in the pinned product-contour theorem
implies that \(B_N(x,t)\) and \(B_N(D/N-x,t)\) are holomorphic
near every compact subset of
\[
 -\frac1{2N}\le\Re x\le1-\frac1{2N},\qquad |\Re t|<\pi,
 \tag{27}
\]
at arbitrary finite imaginary heights. This uses the canonical
factorial itself, not an asymptotic continuation of Stirling's
formula.

Every stationary wire considered here has
\(0<\Re x_e\le1/2\), by (6)--(7). The selected angles have
the strict margin (1), and outside angles equal zero. Since there
are finitely many edges, a small fixed neighborhood of the target
satisfies (27) for every \(N\ge2\). For example, choose all wire
real parts between a fixed positive number and a number strictly
below \(3/4\); the latter is the upper endpoint of (27) at \(N=2\).
Thus the exact halfwire factors have no pole in that neighborhood,
including at \(x=1/2\).

Where the source is traced, the exact joint-lens form still contains
\[
 \prod_v
   \sin t_v\,
   \frac{e^{-iNt_v}}{(1-\eta e^{-iNt_v})^2}\,
   e^{i n_vNt_v^2/(4\pi)}
   \cos(N(1-c_v)t_v),\qquad \eta=(-1)^{N-1},
 \tag{28}
\]
with the actual factors
\[
       N^{|E|}\prod_v\frac{-N^2 C_{N,n_v}}{\pi i},
             \qquad C_{N,n}=e^{\pi i nD^2/(4N)},
 \tag{29}
\]
and every prescribed spectator. On selected lower angular
neighborhoods \(H_v>0\), there is no physical trace pole.
The primitive branch in (4) uses the charge-\(c_v\) exponential:
it is the product of \(e^{-iNt_v}\) in (28) and
\(\tfrac12 e^{iN(1-c_v)t_v}\) from the original cosine.
The other cosine exponential and the denominator in (28) remain
in the exact source. At \(c_v=1\) the two cosine terms coincide
and their coefficients add to one. No branch or current is
deleted by the phase calculation.

The exact source equalities retain all first Hermite normals,
the odd simple node, and the original closing functional.
At a genuine free spectral boundary the compiler requires its
ordinary cardinal polynomial representative instead of (26);
its asymptotic phase has not been identified with (3).
Likewise, a reversed-index kernel retains its different original
phase. The Hessian theorem concerns the same-index phase (4)
with its stated fixed outside angular parameters.

Holomorphy in (27) does not imply that (26) is nonzero, that one
continued factorial asymptotic branch dominates there, or that
the descending disk (25) has nonzero coefficient in the prescribed
relative cycle. Exact factorial zeros, branch frequencies,
connectors and all angular sectors must still be retained.
The established gain is the removal of a local full-phase
degeneracy: a vanishing wire-only Hessian at these admitted folds
is not a caustic of the complete stationary system.

## Direct sources

All four complete source texts were read, their directly used
identities checked, and their hashes verified.

* [Two-square radial primitive lift](research_radial_two_square_primitive_lift.md),
  SHA256 21d9af750653621cc82bd73373a99a138210fc4cdb10407faabcb209505df9ad:
  the actual radial hypotheses, matching/pinning theorem, units,
  and nonsingular lifted constraint/primitive system.
* [Unsummed original network phase](research_unsummed_network_phase_coercivity.md),
  SHA256 b5441bb508d3ffad3274e38dda2d6aeb099d08ae2ab043a0d12c25234e4a1e1e:
  (1)--(4) and Section 5, the same-index incidence phase, original
  zero logarithmic lift and angular derivative normalization.
  Its numerical examples and saved computations are not used.
* [Exact product source contour](research_positive_wire_product_contour.md),
  SHA256 5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230:
  inverse cotangent branch, literal factorial interpolation,
  full-strip holomorphy and distinction between phase and source
  nonvanishing. Its positive-domain stationary graph theorem is
  not extended across the fold by assertion.
* [Joint factorial-lens source](research_joint_factorial_lens_relative_source.md),
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54:
  exact charged top form and normalization, retained full Hermite
  data, free-boundary convention and relative-cycle limitations.

Only written proofs, source-text reads and hashes were used.
No mathematical computation program, numerical evaluation, test
or compilation was run. The adopted two-square note and all
other frozen sources, manuscripts and public documents were
unchanged.
