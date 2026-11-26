# The regular main-meridian period: existing results and the polarization obstruction

31 October 2026. Private continuation; no repository or public file is
changed by this report. The purpose is to locate the remaining selected
classical-factor problem after the scalar volume theorem, rather than
to propose another invariant or reintroduce a uniform nonzero WKB
formula for the reduced state near completeness.

The eight requested inputs were read, together with their relevant
later dependencies: `regularized_kashaev_period`,
`peripheral_normal_period`, `actual_weyl_descent`,
`actual_peripheral_fusion`, `ramified_weyl_fibre`,
`source_corrected_quantum_normal_connection`,
`first_quantum_normal_connection`, and `affine_quantum_a_period`;
also `torsion_initial_rank`, `actual_geometric_normal_period`,
`actual_meridian_companion_source_compatibility`,
`source_symbol_duality_and_presentation`,
`fourier_mellin_actual_source`, `actual_mellin_normal_source_rigidity`,
`mellin_cyclotomic_jet_uniqueness`,
`central_source_freedom_in_regular_profiles`, and
`scaled_meridian_regular_profile`. All names in this paragraph refer
to `.md` files under the workspace's `notes/` directory. Old sentences
saying the volume limit is unproved must now be read with the established
strict/net-twist knot class separated from unrestricted knots.

## 1. The exact objects already available

Fix a zero-framed knot, put

\[
 q_N=e^{\pi i/N},\quad Q_N=q_N^2,\quad M=-q_Nx,
 \quad Y=M^2,\quad U=Y^N.
 \tag{1}
\]

The reduced ADO state is the actual cut scalar. Write it as $f_N(Y)$;
its complete value is $K_N=f_N(1)$. The ordinary-color identities are
$f_N(Q_N^j)=C_j(q_N)$ for $1\le j<N$, with $C_1=1$. The full state is

\[
 \mathcal N_N(M)=\eta_NM^{N-1}\frac{f_N(Y)}{S_N(Y)},
 \qquad S_N(Y)=\frac{Y^N-1}{Y-1},\qquad \eta_N=i^{N+3}.
 \tag{2}
\]

Its shift character is $\kappa=-q_N^{-1}$ and its $N$-cycle sign is
$(-1)^{N-1}$. Neither is an optional gauge choice.

Let $P_N^{\mathrm{ord}}$ be the degree-at-most-$N-2$ polynomial
interpolating the ordinary colors at the nontrivial $N$th roots.
Then the canonical regular remainder is

\[
 p_N=P_N^{\mathrm{ord}}/S_N,\qquad
 R_N=(f_N-P_N^{\mathrm{ord}})/S_N,
 \qquad f_N=S_NR_N+P_N^{\mathrm{ord}}.
 \tag{3}
\]

The remainder is Laurent polynomial. For a fixed $b$-strand braid,
the actual positive ordinary-color trace gives
$|C_j(q_N)|\le D_N\le(N/2)^{b-1}$ and $|p_N(1)|\le D_N$.
Consequently, on the now-proved positive-volume knot class,

\[
 \frac1N\log|K_N|\longrightarrow\frac{V}{2\pi}>0
 \quad\Longrightarrow\quad
 \frac1N\log|R_N(1)|\longrightarrow\frac{V}{2\pi}.
 \tag{4}
\]

This is a proved scalar consequence, not a remaining conjecture for
that class. It says nothing by itself about a fixed meridian
neighborhood. The new nearby-zero theorem rules out such a nonzero
uniform scalar WKB expression for $f_N(M^2)$ itself near $M=1$.

Every specified actual reduced annihilator, after the retained
rational gauge and denominator clearing, supplies

\[
 A_N R_N=b_N,\qquad b_N=-A_Np_N.
 \tag{5}
\]

The Laurent support of $b_N$ lies in one fixed interval and its
coefficients are polynomially bounded in $N$. Its coefficients are
explicit finite sine moments of the ordinary colors. This is a
rootwise source, not a proved single rational function $b(q,Y)$;
its transverse quantum derivatives are not controlled merely by
the ordinary-color bound. Replacing the source by one chosen to
make a candidate solve (5) would change the question.

## 2. The main-meridian normal lattice is already explicit

Put $v_N=(Y-1)f_N$. The primitive minimal actual normal operator $B$
has the proved reciprocity

\[
 BJ=J'B,\qquad J=-Y\mathcal R,\qquad
 J'=\sigma q^{dm}Y^mT^d\mathcal R,\qquad
 \mathcal Rh(Y)=h(Y^{-1}),\quad TY=q^2YT.
 \tag{6}
\]

Here $d$ is the operator order, $m$ is an integer, and
$\sigma\in\{+1,-1\}$ is the retained sign.
The actual state obeys $Jv_N=v_N$. On the marked roots
$Y_r(U)=Q_N^rU^{1/N}$, expand $B_N(U)=B_0+(U-1)B_1+\cdots$ and
$v_N(U)=v_0+(U-1)v_1+\cdots$. Exactly

\[
 (v_0)_0=0,\qquad (v_0)_r=(Q_N^r-1)C_r(q_N),\qquad
 B_0v_1=-B_1v_0,\qquad K_N=N(v_1)_0.
 \tag{7}
\]

The source in (7) is polynomially bounded. The complete functional
and source both lie in the negative Weyl sectors. If the complete
coordinate annihilates the kernel of the negative block, the exact
inverse formula is

\[
 K_N=-N e_0^*B_-^+B_1v_0.
 \tag{8}
\]

Injectivity of $B_-$ suffices, but is not proved for arbitrary actual
operators. The explicit sector dimensions in `ramified_weyl_fibre`
even forbid injectivity for some reciprocity signatures. Generic
rational rank one is a different condition and does not imply this
special-fibre injectivity.

Ramified descent preserves the derivative without requiring either
rank condition. Set $z=(U-1)/(U+1)$, $s=z^2$, and use the specified
unit $U^{-1/(2N)}$ on the input. The invariant lattice is

\[
 \Lambda=\mathbb C[[s]]E_+\oplus z\mathbb C[[s]]E_-.
 \tag{9}
\]

Its special fibre has coordinates $(a_0,b_0)$: $a_0=v_0$ and
$b_0=2v_1-v_0/N$. The original complete evaluations are

\[
 K_N=\frac N2e_0^*b_0,\qquad
 \mathcal N_N(1)=\frac{\eta_N}{2}e_0^*b_0.
 \tag{10}
\]

The factor $ze_-$ is a nonzero generator in this descended fibre.
Setting $z=0$ before taking the invariant lattice would discard it.
An equivariant shear that is identity on the ordinary fibre can
still change $b_0$; the cut functional must be transported as well.

The physical adjacent-color fusion proves this is the actual
boundary lattice. In $w_N=(M-M^{-1})F_N(M)$, a preferred fundamental
parallel acts by $-(T+T^{-1})$, whereas in $v_N=Mw_N$ it acts by
$\kappa T+\kappa^{-1}T^{-1}$. Its complete Casimir residue is
square zero, has rank $N-1$, and has pivotal partial trace equal to
the identity. The knot-dependent coefficient of that residue uses
the derivative at $M=q_N$, not the complete derivative at $M=1$.
The universal nilpotent residue alone does not prove its excitation
by the selected knot state or its identification with a geometric
factor.

## 3. Three different normal directions must be distinguished

There are three exact constructions, with different inputs.

* The derivative in (7) varies the central meridian $U=Y^N$ at a
  fixed root $Q_N$. It is the normal coordinate entering the complete
  ADO value.
* The first quantum-normal connection varies
  $Q=Q_N(1+\epsilon)$ at fixed $Y$, retaining the moving shift. If
  $\mathsf T(Q)$ is the solution transport and $H_0=\mathsf T_0^N$,
  its first term is $H_1+NH_0Y\partial_Y$. After division by $N^2$,
  its kernel-to-cokernel symbol is $U\partial_U$ times the natural
  map $\iota:\ker(H_0-I)\to\operatorname{coker}(H_0-I)$.
* The Mellin construction has base coordinate $X$, shift
  $S_Xg(X)=g(QX)$, and central variable $X^N$. Its quantum-normal
  connection and source quotient concern that polarization.

For the actual finite cut lift the first quantum-normal equation
has the correction determined by $\partial_Z\mathcal A$ of the
same whole preoperator $\mathcal A(Q,Z,Y,T)$, specialized at
$Z=Q^N$. It is not the unsourced connection. The corrected operator
satisfies a Leibniz rule with symbol $\iota$. If
$\iota(v)\ne0$, two central scalar multiples admitting that same
whole lifting rule differ by a constant; the ordinary anchor fixes
the constant. Neither nonzero-symbol nor special-fibre rank follows
from the existence of the reduced scalar at $M=1$.

In the actual Mellin source presentation the selected-symbol
nonvanishing is proved for every knot: an observable row has value
one on the selected section and kills the image of monodromy minus
identity. The bounded cyclotomic quantum-jet theorem goes further.
It fixes the entire rational root Mellin function from the actual
source, starting lattice, pole numerator of degree at most $N$,
and $D(s-1)+1$ quantum jet levels in the stated finite color window.
It requires no rank-one or semisimplicity assumption. Here $D$ is
the meridian exponent span of the fixed recurrence's leading
coefficient and $s$ is its number of collected monomials.
This is an exact uniqueness theorem, not yet a map from a proposed
main-meridian geometric realization.

## 4. The precise Fourier map exchanges two central divisors

Use the generic quantum torus

\[
 \mathcal R_Q=\mathbb C(Q)\langle Y^{\pm1},T^{\pm1}\rangle,
 \qquad TY=QYT.
 \tag{11}
\]

The actual finite-start generating series is
$Z(Q,X)=\sum_{n\ge n_0}C_n(Q)X^n$. Its Fourier map is exactly

\[
 \Phi(Y)=S_X,\qquad \Phi(T)=X^{-1},\qquad
 X^{-1}S_X=QS_XX^{-1}.
 \tag{12}
\]

For $P=\sum_{j,m}a_{jm}(Q)Y^mT^j$, its ordered image is
$\Phi(P)=\sum_{j,m}a_{jm}(Q)Q^{-mj}X^{-j}S_X^m$.
The finite starting point creates the explicit source
$\Phi(P)Z=\mathcal B$, rather than a homogeneous equation. Here
is its full nonvanishing argument in the actual all-knot conventions.
Write $P=\sum_{j=0}^{d_c}a_j(Q,Y)T^j$, with both endpoint
coefficients nonzero after one fixed denominator clearing and shift.
Let $A_c$ be the $Q$-exponent span of the collected Laurent
monomials of $a_{d_c}$. Choose a fixed
$n_0\ge d_c+A_c+1$. If $r>A_c$, distinct monomials of
$a_{d_c}(Q,Y)$ stay distinct after $Y=Q^r$: a collision with
different $Y$ exponents would require $r\le A_c$. Hence
$a_{d_c}(Q,Q^{n_0-d_c})\ne0$.

Termwise summation of the actual color recurrence gives

\[
 \mathcal B(Q,X)=
 \sum_{j,m}a_{jm}(Q)Q^{-mj}X^{-j}
       \sum_{r=n_0}^{n_0+j-1}C_r(Q)Q^{mr}X^r.
 \tag{12a}
\]

The inner sum is empty for $j=0$. The powers of $X$ range from
$n_0-d_c$ to $n_0-1$, and its least coefficient is exactly

\[
 [X^{n_0-d_c}]\mathcal B
       =C_{n_0}(Q)a_{d_c}(Q,Q^{n_0-d_c})\ne0.
 \tag{12b}
\]

The actual fixed-color function obeys $C_{n_0}(1)=1$, so it is
not the zero Laurent polynomial. The product in (12b) is a fixed
nonzero rational function of $Q$ and has only finitely many zeros
and poles. Thus $\mathcal B_N\ne0$ as a rational function of $X$
at every sufficiently large principal root. This excludes only
finitely many levels of the fixed operator and source, not selected
$X$ values. If a negative shift normalization is removed from
$\Phi(P)$, the same left shift is applied to $\mathcal B$; its
nonvanishing is preserved. No asymptotic input is used here.
In (12a)--(12b), $C_r(Q)$ denotes the same fixed-color invariant
in its proved squared-parameter convention $Q=q^2$; it is not a
new choice of colors.

At a primitive level-$N$ root, introduce both pairs of central
coordinates:

\[
 U=Y^N,\quad V=T^N,\qquad
 U_X=X^N,\quad V_X=S_X^N.
 \tag{13}
\]

Then

\[
 \Phi(U)=V_X,\qquad \Phi(V)=U_X^{-1}.
 \tag{14}
\]

Rational functions of the main meridian, with $T$ acting by root
shift, satisfy $V=1$ while $U$ varies. Their Fourier image would
therefore lie on $U_X=1$, with $V_X$ variable. Rational functions
of $X$, on which $S_X$ is root shift, instead satisfy $V_X=1$,
with $U_X$ variable. In the original coordinates this second
divisor is $U=1$, with $V=X^{-N}$ variable.

These two support divisors are different. An isomorphism over the
fixed root center cannot identify modules whose generic central
annihilator ideals are respectively $(V-1)$ and $(U-1)$: their
annihilator ideals would have to agree. Fourier is an isomorphism
of the unlocalized quantum tori, but it does not identify these
two chosen rational realizations by a free renaming of variables.

### 4.1 The finite orbit comparison that does hold

At their intersection $U=V=1$ there is the exact finite Fourier
intertwiner

\[
 \mathscr F_N(h)=\sum_{r=0}^{N-1}h(Q_N^r)X^r
       \quad\text{in }\mathbb C[X]/(X^N-1).
 \tag{15}
\]

Indeed $\mathscr F_N(Yh)=S_X\mathscr F_N(h)$ and
$\mathscr F_N(Th)=X^{-1}\mathscr F_N(h)$. This follows term by
term, using cyclic reindexing only after imposing $X^N=1$.

For the actual meridian state its polynomial image is
$K_N+\sum_{r=1}^{N-1}C_r(q_N)X^r$ modulo $X^N-1$. The Mellin
pole numerator has the specified lift

\[
 (1-X^N)(Z_N+p_{<})
   =\sum_{r=1}^{N-1}C_r(q_N)X^r+K_NX^N,
 \tag{16}
\]

where $p_{<}=\sum_{1\le r<n_0}C_r(q_N)X^r$.
Thus (15) compares the meridian orbit with the residue numerator,
not with a finite value of $Z_N$ at a pole. In particular
$\operatorname{Res}_{X=\infty}Z_N\,dX/X=K_N$.

There is also an explicit linear map from the marked normal fibre
(9) to (16). For $1\le r<N$, recover the ordinary value as
$a_{0,r}/(Q_N^r-1)$ and recover the complete value as
$(N/2)e_0^*b_0$. Substitute those values into (16). For the actual
fibre this produces the actual rational Mellin function. It retains
the complete functional rather than replacing it by the ordinary
normal value, which is zero.

This map loses all other components of $b_0$ and all higher central
meridian jets. It is neither an inverse reconstruction of the
meridian profile nor a transport of its first quantum-normal
operator. It proves the scalar/residue agreement already supported
by the pointing, without granting a module comparison.

### 4.2 The finite clock fibre cannot have the proposed first-order lift

The obstruction is visible before any knot is chosen. Set
$Q=Q_N(1+\epsilon)$ with $\epsilon^2=0$. In the whole quantum torus,

\[
 VU=Q^{N^2}UV=(1+N^2\epsilon)UV,
 \qquad [V,U]=N^2\epsilon UV.
 \tag{17}
\]

Suppose the finite orbit fibre admitted a free matrix lift over the
dual numbers with both central actions reducing to identity.
Then $U=I+\epsilon A$ and $V=I+\epsilon B$, so their commutator is
zero modulo $\epsilon^2$. Equation (17) would instead give
$N^2\epsilon I$, a contradiction in characteristic zero.
Equivalently, invertible $N$-by-$N$ clock matrices with
$TY=QYT$ would have determinants forcing $Q^N=1$, whereas
$Q^N=1+N\epsilon$.

This forbids extending the root Fourier intertwiner as an ordinary
finite free clock-matrix gauge through the quantum-normal direction.
It does not forbid a comparison retaining differential normal
operators, relative sources, or a larger module. The derivative
term in the first quantum-normal construction records precisely
why an off-root shift is not a finite-order linear clock. Any such
bridge must retain that term and its source/co-source.

## 5. The boundary module explains the Mellin selected symbol

The meridian boundary module is

\[
 \Delta_Y=\mathcal R_Q/\mathcal R_Q(Y-1).
 \tag{18}
\]

Localization of the meridian to $\mathbb C(Q,Y)$ kills it, since
$Y-1$ becomes a unit. Its Fourier image is
$\mathcal R_X/\mathcal R_X(S_X-1)$, which survives localization
to $\mathbb C(Q,X)$ as a rank-one trivial difference module.
Consequently the two rational localizations discard different
boundary information.

There is a stronger actual consequence on the covered
positive-volume class. Let $P=\sum_i a_i(Q,Y)T^i$ be any
denominator-cleared polynomial reduced-state annihilator.
The boundary-column argument in `peripheral_normal_period` applies
to the now-proved exponential rate: every coefficient satisfies
$a_i(Q,Q^{-i})=0$ identically. Hence

\[
 P=B(Y-1),\qquad A:=\Phi(P)=\Phi(B)(S_X-1).
 \tag{19}
\]

The order is important: these are right factors. Any fixed initial
$S_X$ shift applied to both $A$ and its source preserves $A(1)=0$.
The actual Mellin equation has $AZ_N=\mathcal B_N\ne0$ for all
sufficiently large $N$. Its canonical homogenization is

\[
 \widehat A=(S_X-\sigma\mathcal B/\mathcal B)A.
 \tag{20}
\]

Both $1$ and $Z_N$ are rational root solutions of (20), and they
are independent over $\mathbb C(X^N)$. Otherwise $Z_N$ would be
central and $AZ_N=Z_NA(1)=0$, contrary to its nonzero source.
Their companion vectors are also independent over $\mathbb C(X)$.
Indeed $J1=(1,1,\ldots)^t$; a relation would force
$JZ_N=Z_NJ1$, hence $S_XZ_N=Z_N$. The fixed field of the primitive
root shift is $\mathbb C(X^N)$, contradicting the preceding
independence. Both vectors are fixed by the solution transport
$\mathsf T_0=C_N^{-1}S_X$ and therefore by its $N$th power $H_0$.
This proves

\[
 \dim_{\mathbb C(X)}\ker(H_0-I)\ge2,
 \qquad \partial_t\det(tI-H_0)\big|_{t=1}=0.
 \tag{20a}
\]

Thus the solution-companion monodromy of (20) has eigenvalue one
of geometric multiplicity at least two, not merely a repeated
characteristic root. All statements are for sufficiently large
levels where the fixed rational source and endpoint coefficients
specialize nontrivially. The argument neither asserts a Jordan
block nor determines the dimension of the entire one-sector.

This is a new consequence of combining the existing boundary-factor
theorem with the established positive volume rate. It concerns this
canonical sourced Mellin presentation, not every minimal meridian
operator or every possible inhomogeneous factor.
The additional constant solution does not belong to the prescribed
starting lattice $X^{n_0}\mathbb C[[X]]$. Its existence in the
rational companion kernel therefore does not contradict uniqueness
of the actual generic sourced series in that lattice. Removing
this homogeneous direction from a companion still requires its
source and lattice comparison; it is not a regular gauge change.

There is no conflict with selected-symbol nonvanishing. The
observable source row is $\ell Jf=Af/\mathcal B$ and satisfies

\[
 \ell J1=0,\qquad \ell JZ_N=1,
 \qquad \ell(H_0-I)=0.
 \tag{21}
\]

It detects the selected direction while ignoring the homogeneous
boundary direction. Thus the existing observable-row theorem is
essentially weaker than, and more appropriate than, a simple-root
test. Simplicity is not an available replacement for it in (20).
The row is the source quotient: it vanishes on every homogeneous
solution of $A$. Its nonzero value on the affine section therefore
does not by itself prove a nonzero projection to a proposed
geometric homogeneous factor of $A$.

An exact actual-unknot example further shows presentation dependence.
Take the genuine annihilator $(T-1)^2$ of the constant meridian
state. Its solution companion is a nontrivial Jordan block, and
the selected vector lies in the image of monodromy minus identity:
its selected symbol is zero. Choose the admissible start $n_0=3$.
Then

\[
 Z=X^3/(1-X),\qquad A=(X^{-1}-1)^2,
 \qquad \mathcal B=X(1-X).
 \tag{22}
\]

The canonical Mellin homogenization has order one in $S_X$, and
its observable row has value one; its selected symbol is nonzero.
Conjugating the meridian operator by $Y-1$ gives the same generic
Jordan obstruction for the normal state. This example does not
claim failure for the primitive minimal meridian operator. It
proves that Fourier transformation together with the actual
finite-start source is not a regular gauge preserving the
meridian companion's selected-symbol test.

## 6. Concrete algebraic comparison criteria, with their missing inputs

There are two useful exact routes. Neither asks for a nonzero WKB
formula for the reduced meridian state across $M=1$.

### A. A shared marked normal kernel

A fixed initial-form torsion certificate can prove generic rational
kernel rank one at every sufficiently large level. Explicitly,
the least $Y$-coefficient polynomial of a rational-coefficient
annihilator must have exactly one occupied root on the grid
$(q_N,Q_N^r)$; the finite binomial-curve test in `torsion_initial_rank`
certifies this uniformly and permits non-toric factors with finitely
many exceptional levels.

Suppose a proposed geometric period is actually placed in that same
kernel, the same saturated ramified lattice, and the same Weyl
equivariance, with the ordinary anchor equal to one. Then it is
$h(U)v_N$ for a central unit with $h(1)=1$. Weyl symmetry gives
$h(U)=h(U^{-1})$, hence $h'(1)=0$. Its two marked fibre coordinates
and the complete functional (10) therefore agree exactly. This
does not require special-fibre injectivity. It is the existing
rigid comparison criterion, not an unconditional construction of
the second period.

Without generic rank one, there is a precise finite lattice test.
Let $K_N^{\mathrm{sat}}$ be the special fibre of the saturated
generic kernel inside (9), let $\pi_+$ record the supplied ordinary
data, and let $\ell_N=(N/2)e_0^*$ on its negative coordinate.
Two lifts with those ordinary data have the same scalar if and
only if

\[
 \ell_N\bigl(K_N^{\mathrm{sat}}\cap\ker\pi_+\bigr)=0.
 \tag{23}
\]

This follows by subtracting lifts, and is checkable by ranks or
minors after a saturated basis has been computed. Replacing the
saturated fibre by the larger special matrix kernel is not
justified. No uniform theorem establishing (23) for every actual
minimal operator has been found in the inspected notes.

To compare whole central profiles, rather than just their marked
complete scalar, the stronger source-corrected first-normal
condition is required: the same whole preoperator, its actual
linear source rule, and a nonzero selected symbol. The algebraic
dual certificate is a row $w$ satisfying
$w(H_0-I)=0$ and $wv\ne0$. It removes central multipliers by the
Leibniz rule, but not arbitrary homogeneous source-kernel additions.

### B. A shared sourced Mellin realization

The bounded cyclotomic-jet theorem supplies a stronger uniqueness
criterion without any rank assumption. A proposed geometric
realization must produce a rational function with the same fixed
starting lattice and the same pole numerator of degree at most
$N$, and a lift through $D(s-1)+1$ quantum levels satisfying the
same finite-window source equation with the actual initial colors.
It then equals $Z_N$ identically, and its residue is $K_N$.

This criterion is finite in the quantum-normal order and retains
every source coefficient. But obtaining that realization is not
the same as applying the generic Fourier map to a rational
main-meridian section; Sections 4--5 give exact reasons why.
The source and cyclotomic lattice must be constructed and carried
through the polarization change.

## 7. What remains for a selected classical main-meridian factor

The existing geometric coefficient calculation supplies a nonzero
transverse formal normal block with the correct marked longitude
action and formal amplitude connection. It does not prove that
the remaining global source pairing survives in the minimal
operator of the summed knot state. The now-proved complete scalar
growth does not supply that missing map by itself.

A useful algebraic target is a nonzero map from the actual normal
module, retaining its source and marked lattice, to the geometric
formal rank-one module on a branch with shift multiplier
$a(h,Y)=L_{\mathrm{geo}}(Y)+O(h)$. If the image of the cyclic
generator is a nonzero formal Laurent series, apply the actual
normal annihilator to that image and inspect its first nonzero
$h$ coefficient. It gives

\[
 B_{\mathrm{cl}}(Y,L_{\mathrm{geo}}(Y))=0.
 \tag{24}
\]

Indeed every finite shift has the leading multiplier
$L_{\mathrm{geo}}^j$, and the first nonzero coefficient of the
image can be cancelled in the geometric function field. Thus a
source-compatible nonzero normal-module map is a concrete
sufficient survival theorem. A local geometric coefficient block
not known to satisfy the *summed* operator does not supply (24).
Here $h=\log Q$ and $q=e^{h/2}$. The notation
$L_{\mathrm{geo}}$ means the geometric multiplier in the same
normal-state character convention as $B$; conversion to the
preferred boundary eigenvalue must retain $\kappa=-q^{-1}$ and
the chosen lift. No longitude sign is removed by (24).

For two supplied affine presentations, the additional source
condition is exact, not an unspecified normalization: after a
homogeneous comparison $G$, the difference of their sources must
be $(\sigma-C)t$. The corresponding augmented map must transport
the selected section, the full cyclotomic/normal lattice, and the
cut row including its affine constant. These are the equations
already written in `actual_geometric_normal_period` Section 8 and
`fourier_mellin_actual_source` Section 6. Rootwise splitting of an
affine system, formal Gaussian equivalence, or matching only the
ordinary fibre does not prove them.

The minimal unresolved task is therefore an actual source/lattice
comparison with nonzero selected geometric image, using either
criterion A or criterion B or an equally explicit replacement.
It is not existence of an ADO annihilator, construction of a
normal-period functional, or scalar volume growth for the proved
knot class. Auxiliary crossing-circle deformation and filling
parameters used in that volume theorem are not the unrolled
main-meridian variable $M$; their established complex packets do
not silently provide this missing comparison.

One concrete route beyond the obstruction is to retain the polynomial
meridian module before inverting $Y-1$, apply the exact generic
Fourier map, and carry the finite-start boundary relation (12a) as
part of the object. A proposed geometric construction would then
have to produce an augmented source-one section in this same
presentation, with the actual prefix, the pole numerator (16),
and the finite quantum-jet certificate of criterion B. These
conditions would prove equality with the actual root Mellin
function, rather than assume equality from its residue. Separately,
the construction must map its nonzero geometric formal normal
block into that sourced presentation and retain its cut pairing;
the first nonzero formal coefficient would then prove (24).
The required quantum-normal transport must allow the derivations
in (17), not attempt the impossible finite free clock lift.

The generic Fourier map, finite boundary source, pole/jet uniqueness,
and local nonzero geometric coefficient block are proved inputs.
The source-preserving map from that block and its selected global
cycle into the same augmented realization is the unproved part
of this route. A construction that defines its geometric section
by dividing by or interpolating the already known $K_N$ would
not supply that map or a classical-factor proof.

No new general geometric-factor theorem is claimed here. The exact
new deductions preserved for continuation are the central-divisor
separation, its finite-orbit comparison and first-order obstruction,
and the forced multiple eigenvalue-one sector in the canonical
Mellin presentation of a positive-volume knot.
