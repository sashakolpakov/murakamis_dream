# Exact finite-window conditioning near rational phase colors

Private written proof, 16 November 2026.

For the complete finite-level repeated-turn equations, a fixed window
near a rational phase has finitely many analytic coefficient germs in
\(h=1/N\). A nonzero full-column minor gives polynomial conditioning
on its leading-coefficient unit chart. This conclusion includes all
physical first normals. It does not prove that such a minor exists
for every active product, and it does not replace the boundary data
required by a window with lower-rate data that have not been supplied.

## 1. A fixed actual window and its supplied data

Use the original repeated-turn source
\[
 \mathcal Y_N=U_\tau Z_N,\qquad \tau\in\{1,-1\},
 \quad q=e^{\pi i/N},\quad
 C_N(u)=2\cos(2\pi u+\pi/N).
 \tag{1}
\]
The column \(Z_N\), every cleared full-step row, and all retained
source and recovery equations are those of the pinned full-step
interface. All counts and signed powers are fixed. Microscopic
parameters \(\boldsymbol\alpha\) remain in a fixed bounded complex
neighborhood; they are not independent physical colors being
silently quotiented.

Fix a reduced rational phase
\[
             0<a/b<1/2,\qquad \gcd(a,b)=1,\qquad
             v_*=\exp(2\pi i a/b).
 \tag{2}
\]
Let
\[
 j_N=\lfloor Na/b\rfloor .
 \tag{3}
\]
Choose a fixed finite set of translated exact rows near \(j_N\).
Include their value and first-\(u\)-normal equations. Specify a
fixed finite list of unknown shifted components and their normals,
forming a packet \(X_N\) of dimension \(d\). Every other shifted
component appearing in the chosen rows must either be included in
\(X_N\) or put in a separately specified supplied packet \(B_N\).
Any genuine inhomogeneous source packet is denoted \(F_N\).
Thus the actual finite equations have the form
\[
          \mathsf A_N X_N=F_N-\mathsf L_N B_N .
 \tag{4}
\]
Rows containing additional unknowns cannot be used in (4) until
those unknowns have been accounted for. Repeated occurrences of the
same physical component are identified. The window is interior
for sufficiently large \(N\), so all its spectral nodes are double
and the \(u\)-normal and spectral normal differ by uniformly
invertible factors.

The choice of supplied packet is part of the assertion. For example,
if a two-sided recovery uses a right boundary packet known only to
have size \(e^{C N}\), (4) retains that size. It is not an initial-value
transport bound at a smaller left boundary rate.

## 2. Exact residue classes and meromorphic coefficient germs

**Lemma 1.** Split the levels into residue classes modulo a fixed
multiple of \(b\). On each such class there is a fixed rational
\(\delta\in(-1,1]\) such that every shifted physical angular color
in the window is exactly
\[
 v_{j_N+k}=q^{2(j_N+k)+1}
               =v_*q^{\delta+2k},\qquad
 \delta=2\lfloor Na/b\rfloor+1-2Na/b .
 \tag{5}
\]
After splitting further for any retained parity or rational carrier
phases, every coefficient of \(\mathsf A_N,\mathsf L_N\) is the
restriction of a meromorphic germ
\[
 \mathsf A(h,\boldsymbol\alpha),\qquad
 \mathsf L(h,\boldsymbol\alpha)
 \tag{6}
\]
at \(h=0\), with at most a finite-order pole. On a fixed valid
coefficient chart a common power \(h^s\), \(s\ge0\), makes these
matrices holomorphic and bounded on a slightly smaller chart.

*Proof.* If \(N\) increases by \(b\), the floor in (3) increases
by \(a\), so \(\delta\) is unchanged. Formula (5) follows without
approximation.

The raw interface coefficients are obtained by finitely many rational
operations, shifts and polynomial coefficient clearings from
\[
 q^{\pm1},\quad h,\quad v^{\pm1},\quad
 w_i=2\cosh(\alpha_i h),\quad
 P_N(w_i)=4\cosh^2(\alpha_i/2).
 \tag{7}
\]
Removable scalar powers of \(h\) in their definitions are retained
with their exact limits. Substitution of (5) makes (7) holomorphic
in \(h,\boldsymbol\alpha\) near \(h=0\). Any remaining coefficient
denominator gives a meromorphic germ; on the stated coefficient
chart its nonremovable part is a unit after a finite power of
\(h\) is extracted. The numbers of operations and shifts are fixed.

For the normal rows, ordinary differentiation at fixed \(N\) acts on
the coefficient angular variable by
\(2\pi i v\,\partial_v\). It preserves this meromorphic class.
The ordinary residual is a multiple of \(P_N(C_N(u))\), so its
value and first derivative do vanish at the grid; no off-grid
homogeneous equation is used.

The interface operator coefficients do not require a varying
Gaussian carrier to be discarded. If a chosen row normalization
retains \(\eta=(-1)^{N-1}\) or
\[
 \kappa=\exp\{\pi i(N-1)^2/(2N)\}
             =-i^N e^{\pi i h/2},
 \tag{8}
\]
enlarge the modulus to include \(4\). If physical crossing
values at the moving center are explicitly included as coefficient
factors, the additional carrier is
\((-1)^{n(j_N+k)}q^{n(j_N+k)(j_N+k+1)}\).
After (5), its phase is a rational multiple of \(\pi N\), a
residue-class constant, and an analytic \(O(h)\) phase.
A modulus divisible by \(4b^2\) suffices for these fixed integer
powers. More generally choose a common multiple for every fixed
rational phase actually retained. This finite refinement does not
change the source or its modulus on physical levels.

No meromorphic-germ assertion is made about \(X_N,B_N,F_N\)
themselves. They remain the actual possibly exponentially large
source packets. \(\square\)

The coefficient-chart qualification is substantive. At a parameter
where a proposed denominator loses its leading unit, re-clear the
original rows or choose another valid coefficient chart before
applying the lemma. Nonunit physical clearing factors are not
canceled in the original algebra.

## 3. Nonzero actual minors give polynomial recovery

**Theorem 2.** Fix one residue class and one coefficient chart from
Lemma 1. Suppose \(h^s\mathsf A(h,\boldsymbol\alpha)\) is holomorphic
and bounded there, and some selection of \(d\) actual rows has
determinant
\[
 \det \widehat{\mathsf A}_0(h,\boldsymbol\alpha)
    =h^\nu\{c(\boldsymbol\alpha)+h r(h,\boldsymbol\alpha)\},
 \qquad \nu\ge0,
 \quad \widehat{\mathsf A}=h^s\mathsf A .
 \tag{9}
\]
On a compact parameter set where
\(|c(\boldsymbol\alpha)|\ge c_*>0\), there is a left inverse of
the full matrix \(\mathsf A_N\) with norm at most \(C N^K\),
for a fixed \(K\). Consequently the original packet satisfies
\[
       \|X_N\|\le C N^{K'}
                    \bigl(\|F_N\|+\|B_N\|\bigr).
 \tag{10}
\]
All quantities on the right are the supplied packets of (4).
The constants and exponents are uniform on that fixed compact
unit chart.

*Proof.* After decreasing the \(h\)-disk, the expression in braces
in (9) has modulus at least \(c_*/2\). The entries of the adjugate
of \(\widehat{\mathsf A}_0\) are uniformly bounded, since its size
is fixed. Its inverse is therefore \(O(h^{-\nu})\). Select those
rows of \(h^s\mathsf A X\), invert, and retain the factor \(h^s\)
on the right. This defines a left inverse of the full matrix;
one may take \(K=\max(0,\nu-s)\).
The remaining coefficient matrix \(\mathsf L_N\) is bounded by a
fixed power of \(N\) by Lemma 1. Applying the left inverse to (4)
proves (10). No equation or source channel has been dropped:
the selected rows recover the packet, while the other actual rows
remain its compatibility equations. \(\square\)

For fixed parameters, this gives an exact eventual dichotomy.
Either at least one full-column minor is a nonzero meromorphic
germ, in which case the rank is full and the conditioning is
polynomial for all sufficiently large levels in that residue
class, or every such minor is the zero germ. In the latter case
the chosen matrix is rank deficient for all sufficiently small
\(h\) in its coefficient chart. This is rank of the specified
finite window; it is not a statement that the entire global
source problem has a free parameter.

For varying parameters, a nonzero minor as a germ in
\((h,\boldsymbol\alpha)\) does not give uniform conditioning on
an arbitrary compact set. The leading coefficient in (9) can
vanish there, and parameters may approach its zero set very
rapidly with \(N\). The unit-chart hypothesis must be verified
or replaced by a separate stratified estimate.

If the supplied data obey uniform bounds
\[
 \|F_N\|\le e^{N A_F+o(N)},\qquad
 \|B_N\|\le e^{N A_B+o(N)},
 \tag{11}
\]
then (10) gives only
\[
                \limsup_{N\to\infty}N^{-1}\log\|X_N\|
                                  \le\max(A_F,A_B)
 \tag{12}
\]
along the residue class. Thus a right endpoint ceiling larger
than the incoming rate remains larger in this result.
All fixed parameter derivatives satisfy the same statement if
the unit bound holds on a larger parameter neighborhood and
the supplied source bounds hold there, by Cauchy's formula.
The actual first physical normals are already entries of (4).

## 4. What must still be proved for the complete repeated-turn source

The matrices in this note are formed from the full finite-\(N\)
rows and their normal equations, with any original recovery and
source constraints used in the window explicitly included.
They are not formed from a principal scalar certificate. The
rank-loss theorem gives the same warning at a single row:
the first-normal block can determine a missing value without
determining its normal, whereas further aligned rows can restore
the full rank.

For fixed active products, finitely many rational exceptional
phases and finitely many residue classes therefore reduce local
polynomial conditioning to exact nonvanishing assertions of
the form (9), together with honestly supplied boundary packets.
This note does not establish those assertions for every product
or every minimal resonance core. Nor does it prescribe a fixed
window that must work universally.

An identity of all candidate minors may reflect a genuine
remaining local channel, an unnecessarily large unknown packet,
or extra solutions introduced by a nonunit clearing. It must be
examined using the original source constraints. Conversely a
nonzero minor may arise from small quantum terms even when the
classical phase is exceptional. The arithmetic observation (5)
does not decide either outcome.

No rate for a general repeated-turn output, no disappearance
of a clearing component, and no geometric gap is inferred.
The conditioning statement is useful only after its exact
rank and boundary-data premises are met.

## 5. Direct sources

The complete direct source texts were read at the following pins,
with the directly used formulas and hashes checked:

* [Full-step repeated-turn tensor interface](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398:
  exact polynomial row construction, rational coefficient field,
  source and recovery columns, full-normal residual interpretation
  and retained original carriers.
* [Exact rank loss and the physical normal](research_simple_rank_loss_full_normal_transport.md),
  SHA256 307a26ca51fc9b0cc7bff689f52a873a49d7773406e67d243ec71021401e4694:
  the exact value-and-normal equations, complete aligned-row
  criterion and the distinction between local and global recovery.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or build was
run. Adopted notes and public manuscripts are unchanged.
