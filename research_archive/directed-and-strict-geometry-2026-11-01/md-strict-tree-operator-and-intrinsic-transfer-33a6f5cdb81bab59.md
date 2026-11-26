## 7. The geometric factor selected by the actual recurrence

The geometric theorem identifies the curve already selected by the
full asymptotic expansion of the original strict-tree invariant.
This extends the operator consequence beyond trees whose junctions
all carry crossing circles. It requires no quantum estimate for the
newly drilled diagram: the quantum source remains the original
strict presentation.

Fix an oriented strict ordered Conway knot presentation \(D\), with
its original cut, endpoint orders, framing and signed integral
crossing powers. Assume the powers are independently sufficiently
long for the [filled-meridian theorem](actual_main_meridian_filled_volume.md)
and the geometric theorem above. The entire diagram and every power
are fixed before \(N\) tends to infinity. All original knot-pattern
and absence-of-internal-component qualifications remain in force.
Both level parities and all sufficiently large composite levels are
included.

Write \(F_N(M)\) for the actual zero-framed reduced ADO invariant,
with
\[
 q_N=e^{\pi i/N},\qquad M=-q_Nx,\qquad F_N(1)=K_N(K).
 \tag{O1}
\]
Here \(x\) is the raw highest-weight parameter, distinct from an
internal normalized index \(x_e\). The marked complete meridian is
\(M=1\), and \(X_e=e^{2\pi ix_e}\) denotes the original physical-edge
variable.

Let
\[
 P(q,M,T)=\sum_{j=0}^{d}a_j(q,M)T^j,\qquad
 a_j\in\mathbb C(q,M),\qquad TM=qMT,
 \tag{O2}
\]
be any specified nonzero fixed operator that annihilates the whole
function \(F_N(M)\) at every sufficiently large level. The shift \(T\)
replaces \(M\) by \(qM\). Such an actual all-level annihilator exists
by the [finite-sum construction](finite_sum_annihilator.md); it is not
defined by fitting the complete values or adjoining a desired factor.
An operator with negative shift powers can first be multiplied by
a power of \(T\).

Clear fixed rational denominators, remove the common \(q-1\)
valuation of the coefficients, and denote the resulting first nonzero
classical symbol by \(P_0(M,L)\). Let
\(A_{\mathrm{geom},\mathbb C}(M,L)\) generate the Laurent prime of the
actual geometric eigenvalue germ through \((1,-1)\), in the preferred
meridian and longitude of the original knot. The longitude coordinate
is its eigenvalue on the \(M\) line, equivalently the inverse
eigenvalue on the source \(M^{-1}\) line.

Then
\[
 \boxed{\displaystyle
 A_{\mathrm{geom},\mathbb C}(M,L)\mid P_0(M,L)
 \quad\text{in }\mathbb C[M^{\pm1},L^{\pm1}].}
 \tag{O3}
\]
Thus every genuine all-level annihilator has the same selected
irreducible geometric factor in its first classical symbol.

### Proof and normalization

The [filtered characteristic theorem](actual_main_meridian_filtered_characteristic.md),
Sections 2–6, already applies to the full strict long-filling class,
including arbitrary bare components. It proves the complete
microscopic expansion with its degree filtration on all the finitely
many translated parameter charts needed by (O2). This shifted-chart
statement follows from the exact source and its endpoint estimates,
not from continuation of an asymptotic formula on a single disk.

The normalized full state is
\[
 \mathcal Z_N(s)=\frac{F_N(q_N^s)}{F_N(1)H_N(s)},\qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)}.
 \tag{O4}
\]
It retains the exact modified-dimension gauge
\[
 d_N(M)=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}},\qquad
 d_N(1)=\eta_N/N,\qquad
 \frac{d_N(q_N^s)}{d_N(1)}=H_N(s)^{-1}.
 \tag{O5}
\]
Here \(\eta_N=i^{N+3}\). Put \(f(M)=M-M^{-1}\). The operator on the
full state has shift coefficients
\[
 \widetilde a_j(q,M)
 =a_j(q,M)(-1)^j\frac{f(M)}{f(q^jM)}.
 \tag{O6}
\]
After multiplication on the left by
\(\prod_{j=1}^{d}f(q^jM)\), its first classical symbol is
\(f(M)^dP_0(M,-L)\). The meridian divisor and the shift sign are
therefore present before any formal cancellation.

The filtered theorem defines the selected critical value \(S(t)\)
using the original phase and the insertion
\[
 \sum_{e\in\mathcal E_T}
 [2J(x_e)-J(x_e+t)-J(x_e-t)]
 +\frac{\pi i a(D)}2t^2.
 \tag{O7}
\]
Its expansion has coefficient of order \(N^{-r}\) of degree at
most \(r+1\) in \(s\). The top-degree coefficients come from \(S\);
lower Gaussian amplitudes cannot change them. With
\(\mathcal S(u)=\pi i[S(u/(\pi i))-S(0)]\), the exact operator
equation and this filtration give the formal domain identity
\[
 f(e^u)^dP_0(e^u,-e^{\mathcal S'(u)})=0.
 \tag{O8}
\]
The full argument, including injectivity of the substitution
\(u=hs\), is in
[the all-circle operator proof](actual_all_circle_geometric_characteristic.md#11-the-geometric-factor-of-an-actual-quantum-recurrence),
Section 11.3. That argument depends on the filtered source expansion
and the exact gauge, not on the absence of bare vertices. The
nonzero series \(f(e^u)^d\) can be cancelled in this proved integral
domain identity.

The new geometric input identifies its entire selected germ:
\[
 -e^{\mathcal S'(\log M)}
 =-M^{a(D)}\prod_{e\in\mathcal E_T}
              \frac{M^2-X_e(M)}{1-M^2X_e(M)}
 =L_{\mathrm{geom}}(M).
 \tag{O9}
\]
The zero-circle elimination above preserves the whole critical-value
germ and the original physical-edge set. Its ordered boundary-group
anchor identifies the original filled geometric representation.
The preferred-longitude sign is fixed at that filled knot point.
Thus (O9) is not inferred from the cusp tangent or from a choice among
unmarked exponentiated solutions.

It follows that \(P_0\) vanishes on the geometric eigenvalue germ.
Its Laurent evaluation kernel is a nonzero prime and contains no
nonzero polynomial in \(M\) alone, because \(M\) varies. It is
therefore a height-one prime in a Laurent polynomial unique
factorization domain, proving (O3).

If the operator coefficients lie in \(\mathbb Q(q,M)\), contract
that same germ prime to \(\mathbb Q[M^{\pm1},L^{\pm1}]\). Its
irreducible generator divides the rational symbol. Its complex
factorization contains the selected geometric factor and any
conjugate factors required over \(\mathbb Q\); an individual complex
component need not itself be defined over \(\mathbb Q\).

## 8. Transfer to presentations with net twists and arbitrary closures

The conclusion is intrinsic to the zero-framed knot with its marked
peripheral curves. Suppose the
[ordered net-twist reduction](actual_conway_net_twist_volume.md) gives
an actual ambient isotopy from the input knot to a strict knot
presentation covered by Section 7. The isotopy carries the knot
orientation, meridian, preferred zero-linking longitude and cut mark.
Correcting any transported ribbon framing to zero gives exactly the
same reduced ADO function \(F_N(M)\) at every level and every
meridian value where it is defined. Its rational continuation is
therefore the same function as well.

The geometric eigenvalue germ is also the same under this marked
isotopy. An actual all-level operator for the input family thus
satisfies the hypotheses of Section 7 for that same intrinsic
family. Its first classical symbol contains the selected geometric
factor. This transfers the factor statement without identifying
presentation-specific recurrence formulas or their unreduced
polynomial representatives.

The same argument applies to the
[arbitrary-closure reduction](actual_conway_arbitrary_closure_volume.md)
when its hypotheses yield one covered strict knot factor and only
unknot factors. In particular, under its long surviving-factor
hypotheses, a hyperbolic knot input has exactly that form. Removing
the exhibited unknot summands is an actual orientation-preserving
ambient isotopy. The preferred peripheral pair is carried by the
induced map of exteriors. No multiplicativity assertion for quantum
growth over connected sums is required.

For a fixed original expression there are finitely many recorded
reduction and parity branches. If a uniform net-weight statement is
desired, take the maximum of the strict source and geometric
thresholds over those finitely many possible strict outputs. The
threshold concerns their surviving signed net powers. Large
individual powers that cancel to a short surviving power do not
satisfy it. This does not assert that an earlier, smaller
complete-value threshold automatically supplies the stronger
moving-meridian hypotheses.

The integer \(a(D)\) and the individual edge factors in (O9) are
computed on the covered strict diagram. They are not claimed to
equal those read from an unreduced input presentation term by term.
The preferred geometric longitude and its selected irreducible
factor are the intrinsic objects that transfer.

The conclusions concern one irreducible geometric factor, not the
full A-polynomial, its multiplicity, or an equality of quantum
operator ideals. They do not provide a fixed-\(M\) large-level WKB
theorem, nonvanishing through ordinary-color resonances, or a
general short-twist theorem. The wider quantitative all-circle
alternatives remain available under their own source and geometric
hypotheses; this section neither narrows those results nor extends
them to arbitrary short bare-junction fillings.
