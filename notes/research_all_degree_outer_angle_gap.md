# The outer angular gap at every degree

The real angular part of an isolated filled vertex admits one estimate
whenever the degree or the nonzero crossing power has magnitude at least
three.
The argument uses the exact finite kernel before any contour deformation.
It applies to every retained subset of wire indices, so it can be used
in the trace-first contour construction.

Fix integers \(d\geq1\) and \(|n|\geq1\), with
\(\max(d,|n|)\geq3\), independently of the level \(N\). Write
\[
 P_{d,n,N}(\mathbf u)
 =\phi_N^{(t)}\left[R^n\prod_{j=1}^dK_N(t,u_j)\right],
 \qquad
 K_{N,I}(t,u)=\sum_{k/N\in I}e_k(-2\cos t)e_k(-2\cos u),
\]
where each retained set \(I\) is contained in the original low-index
range. The Newton polynomials \(e_k\), the original crossing \(R\),
and the trace \(\phi_N\) have the conventions of
[the finite-source proof](../papers/circle-tree-volume/finite-bounds.tex).
Let \(M_{d,n}\) denote the selected real action defined in
[the action-gap theorem](research_isolated_vertex_action_gap.md).

**Proposition.** The contribution to the original finite trace from
the real angular nodes \(2\pi/3\leq |t|\leq\pi\), with arbitrary
retained low-index subsets in its \(d\) wires, has absolute value at most
\[
 C_{d,n}N^{A_{d,n}}\exp\{Nd\psi(2\pi/3,0)\}.
 \tag{1}
\]
This includes the first normal at every repeated spectral root and is
uniform for all real remaining boundary angles. Moreover,
\[
 d\psi(2\pi/3,0)<\frac{4d}{5}
 <\frac{5d}{6}<M_{d,n}.
 \tag{2}
\]
Thus the omitted angular region has a strict gap of more than
\(d/30\) below the selected action. Both level parities and both
signs of \(n\) are included.

**Proof.** Put
\[
 J(x)=\int_0^x\log|2\sin(\pi v)|\,dv,\qquad
 g(x)=J(2x)-4J(x).
\]
For a low wire index \(x=k/N\), the real Newton bound, including
moving zeros, gives
\[
 |e_k(-2\cos u)|\leq CN^A e^{Ng(x)}
 \qquad(-\pi\leq u\leq\pi).
\]
At the trace angle, the product of this bound and the corresponding
Newton bound has rate
\[
 A(x,r)=J(r+x)-J(r-x)+J(2x)-6J(x),
 \qquad r=\frac{\pi-|t|}{2\pi}.
\]
[The real-angle theorem](research_terminal_real_angle_tail.md),
Section 2, proves the pointwise inequality
\[
 A(x,r)\leq\psi(2\pi/3,0)
 \qquad(0\leq x\leq1/2,\ 0\leq r\leq1/6).
\]
This is a bound on each summand. Consequently the same bound, with
a polynomial prefactor, holds for every retained subset; no cancellation
in the full kernel is being assigned to a partial sum. Taking the
product over the \(d\) wires gives the exponent in (1).

As a polynomial in \(z=-2\cos t\), this product has degree at most
\(d(N-1)\). The outer angular region is the spectral interval
\([1,2]\). Markov's inequality on this fixed interval bounds its
first \(z\)-derivative at polynomial cost. The original fixed signed
crossing power and the weights of the finite Hermite trace also have
polynomial bounds. Applying the original trace formula proves (1)
with every normal term retained.

It remains to compare this rate with the selected action. For positive
integers \(a,b\) with \(a+b>2\), the action-gap theorem proves
\[
 \frac{M_{a,b}}a=\frac{M_{b,a}}b.
 \tag{3}
\]
It also proves strict increase of \(M_{a,b}\) in the positive real
crossing parameter \(b\), wherever the selected branch exists.
For \(n\geq3\), that branch exists for fixed degree \(n\) and every
real crossing parameter between \(1\) and \(d\). Hence
\[
 \frac{M_{d,n}}d
 =\frac{M_{n,d}}n
 \geq\frac{M_{n,1}}n
 =M_{1,n}
 \geq M_{1,3}.
 \tag{4}
\]
If instead \(d\geq3\) and \(n=1\) or \(2\), monotonicity in the
crossing parameter followed by the same duality gives
\[
 \frac{M_{d,n}}d\geq\frac{M_{d,1}}d
 =M_{1,d}\geq M_{1,3}.
 \tag{5}
\]
The strict rational bounds
\[
 \psi(2\pi/3,0)<4/5,
 \qquad M_{1,3}>5/6
\]
are established in Section 4 of the real-angle theorem and its
[outward-arithmetic verifier](../experiments/audit_terminal_real_angle_tail.py).
Inequalities (2) follow. Negative crossing powers have the conjugate
selected action and the same real part. \(\square\)

This proposition settles the outer-angle hypothesis of
[the scaled contour lifting theorem](research_scaled_wire_contour_lifting.md)
at the fixed cutoff \(T=2\pi/3\). Its central contours, wire endpoints,
and lattice corrections still require their own estimates. Equation
(3) is an identity of classical actions; no equivalence between the
quantum sources with interchanged degree and crossing power is used.
