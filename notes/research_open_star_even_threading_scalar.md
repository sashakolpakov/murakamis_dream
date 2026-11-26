# Even threading on the original open marked source

Private research note, 17 November 2026. The closed auxiliary trace in
the actual threading calculation remains valid with every core boundary
index fixed. Consequently a relatively unlinked even thread acts by two
on the whole same-colored open source, including its literal mark and
every meridian jet. This rules out an open-source defect of that specific
kind; it makes no assertion about a normal derivative before root
specialization or a varying-center relative pushforward.

## 1. Exact source and relative linking

Fix
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad N\geq2,\quad D=N-1,
 \qquad x=q^\alpha=-M/q,\quad U=M^{2N}=x^{2N}.                 \tag{1}
\]
All statements below are identities of meromorphic germs in \(M\ne0\)
at this fixed \(q\). Use the original balanced bases on \(V(x)\) and its
standard dual
\[
                 V(x_D),\qquad x_D=x^{-1}Q^{-1}.              \tag{2}
\]
The unrolled lifts, crossing and turned-crossing matrices, pivot
\(g_b=x^{1-N}Q^{-b}\), and all scalar normalizations are unchanged.

Let \(S\) be a three-ball containing a finite oriented core diagram with
boundary on \(\partial S\). Every strand has the color in (1), with (2)
on its oppositely oriented presentation. Allow the original ordinary
turns, balanced polynomial Casimir coupons \(f_v(\Omega)\), and the
literal marked cap. Coupon coefficients may themselves be meromorphic
in \(M\). A balanced box has zero total oriented boundary charge: the
oriented strands can be continued through its interior as a one-chain.
No diagonalization of a coupon or deletion of its repeated-root data is
performed. In particular the marked cap is exactly
\[
 \operatorname{ev}_R^{\mathsf D}(w_b\otimes w_a^{\rm dual})
       ={x^a\over N^2},\qquad
 \mathsf D_{ab}={x^D Q^a\over N},\qquad 0\leq a,b\leq D.     \tag{3}
\]
It has no Kronecker support condition and is not assumed to be a Hopf
intertwiner. Denote the resulting open array by
\(\mathcal K^S_{\mathbf b;\mathbf a}(M)\); every input and output index
in the multi-indices ranges independently over \(0,\ldots,D\).

Let \(\gamma\subset\operatorname{int}S\) be a closed oriented framed
auxiliary loop disjoint from the diagram and its finitely many disjoint
coupon boxes. Choose an oriented Seifert surface \(\Sigma\subset
\operatorname{int}S\), with \(\partial\Sigma=\gamma\), avoiding those
boxes and transverse to the ordinary strands. Such a surface exists:
removing finitely many interior balls from a ball leaves first homology
zero, and a null-homologous oriented knot bounds an oriented surface
there. Define
\[
              \ell_S(\gamma)=\Sigma\mathbin{\cdot} C_S,       \tag{4}
\]
where \(C_S\) is the oriented core one-chain, completed inside each
balanced coupon box. A different completion has the same intersections
because \(\Sigma\) avoids the boxes. Two choices of \(\Sigma\) differ
by a closed two-cycle bounding in \(S\); its intersection with \(C_S\)
is zero since \(\partial C_S\subset\partial S\). Thus (4) is
well-defined. It is the linking number with any oriented completion
outside \(S\). That outside completion is only a topological way to
compute (4); it does not contract any quantum boundary index. In
particular, merely placing \(\gamma\) inside \(S\) does not imply
\(\ell_S(\gamma)=0\).

Thread \(\gamma\) by the actual annular polynomial
\[
 C_0=2,\qquad C_1=W,\qquad C_{n+1}=W C_n-C_{n-1},             \tag{5}
\]
where \(W\) is the original fundamental color and products mean framed
parallels. Keep all other tensors fixed, and call the resulting array
\(\mathcal K^{S,\gamma}_{\mathbf b;\mathbf a}\) when the threading
degree is \(2N\).

## 2. Entrywise threading theorem

**Theorem.** For every such source and every choice of its boundary
indices,
\[
 \boxed{\quad
 \mathcal K^{S,\gamma}_{\mathbf b;\mathbf a}(M)
  =\bigl(U^{\ell_S(\gamma)}+U^{-\ell_S(\gamma)}\bigr)
       \mathcal K^S_{\mathbf b;\mathbf a}(M).
 \quad}                                                       \tag{6}
\]
This holds at every \(N\geq2\), for either parity, arbitrary auxiliary
framing, and the complete original marked array. It does not require
the open array to be nonzero or scalar.

*Proof.* The integral Weyl exact sequences in the first direct source
give, at the specified root and without dividing by \([N]\),
\[
             C_{2N}([W])=[\mathbb C_{2N}]+[\mathbb C_{-2N}],   \tag{7}
\]
where \(\mathbb C_h\) has \(H=h\), \(K=q^h\), \(E=F=0\).
Here is why that identity applies to the present open array. Fix all
core boundary indices before summing the internal indices. Use bases
adapted to a submodule filtration on the auxiliary color, and dual
flags on reversed auxiliary pieces. Each auxiliary crossing, inverse
crossing and pivot preserves that filtration, with tensor positions
exchanged at crossings. Core coupons, including (3), act on the other
factors. A contributing auxiliary state can move only in the permitted
filtration direction; closing that auxiliary component forces it to
return to its initial grade. Its grade is therefore constant throughout
the component. The sum splits into the graded-piece evaluations with
the same fixed core boundary indices. This proves the required
additivity. Tensor-color identities on the auxiliary strands identify
tensor products with framed parallels, including at auxiliary
self-crossings. Nothing in this argument closes the core, applies
Schur's lemma, or moves the mark by Hopf naturality.

For \(h=\pm2N\), the nilpotent part of the original \(R\) is the
identity. Its Cartan part on a primal weight basis is
\[
 q^{hH/2}w_a=q^{\pm N(\alpha-2a)}w_a
                =x^{\pm N}w_a.                              \tag{8}
\]
Thus a single crossing is a scalar times the flip, independently of
the core index; an inverse crossing has the reciprocal scalar. On the
actual dual (2) the scalar is
\[
                    x_D^{\pm N}=x^{\mp N},                   \tag{9}
\]
because \(Q^N=1\). The \(Q^{-1}\) in (2) has been retained before
taking the \(N\)-th power. On \(\mathbb C_{\pm2N}\) the pivot,
self-braiding and twist are all exactly one:
\[
 q^{(1-N)h}=1,\qquad q^{h^2/2}=1,\qquad
                    q^{h^2/2+(1-N)h}=1.                      \tag{10}
\]

The scalar products in (8)--(9) agree on the two sides of any balanced
coupon. They also cancel on a primal-dual cup or cap. This assertion
holds for every entry of (3): it uses only the two reciprocal scalar
factors, not a nonexistent intertwining property of \(\mathsf D\).
It therefore permits auxiliary unlinking with all original coupon
arrays, pivots and boundary indices unchanged. A crossing change with
an oriented core strand has ratio \(x^{\pm2N}\), with the reciprocal
for the reversed orientation. Unlinking \(\gamma\) while fixing the
core boundary records exactly the intersection number (4), so the
\(\mathbb C_{\pm2N}\)-colored evaluation is
\(x^{\pm2N\ell_S}\mathcal K^S_{\mathbf b;\mathbf a}\).
Equivalently one may compute the signed crossing sum using an outside
oriented completion of \(C_S\); the sum is \(2\ell_S\), and no
boundary contraction is involved. After unlinking, the remaining
one-dimensional auxiliary knot, with any framing, has value one by
(10). Summing its two colors in (7) proves (6). \(\square\)

## 3. All meridian jets and the remaining comparison

If \(\ell_S(\gamma)=0\), define the proposed open defect by
\[
 \mathcal D_{\gamma,N}(M)=\mathcal K^{S,\gamma}(M)
                                      -2\mathcal K^S(M).
\]
Then
\[
 \mathcal D_{\gamma,N}\equiv0,\qquad
 (M\partial_M)^r\mathcal D_{\gamma,N}\equiv0
                   \quad\hbox{for every integer }r\geq0.     \tag{11}
\]
These are entrywise meromorphic identities. Hence every Laurent
coefficient, any common prescribed polar subtraction, and every
ordinary meridian jet at a regular point also vanish. Arbitrary
exterior contractions and parameter derivatives preserve (11),
including all original Casimir normal data already present in the
coupons. This is stronger than the vanishing of one exterior scalar
pairing. If \(\ell_S\ne0\), (6) still specializes to multiplier two
at \(M=1\), but the assertion about all meridian jets is not made.

The theorem is at fixed root \(q\). It does not identify an off-root
family, compute a derivative normal to the root divisor, or assert
that its first such derivative is nonzero. Nor does it exclude a
relative pushforward with varying central character and a geometric
semiclassical saddle. It excludes the specific proposal that leaving
this same-colored source open can retain a nonzero relatively unlinked
even-thread defect or recover it by meridian differentiation alone.

## Complete direct sources

Both texts were read in full for this proof. The first supplies the
integral Weyl identities and original auxiliary trace normalization;
the second supplies the actual dual, turns and non-Hopf marked cap.

- [The actual ADO threaded character](ado_threaded_shadow.md),
  SHA256 `c97b10ee6fa4d629e5f5e21297eec78acf236a7f136628b1153e97b413b6910d`.
- [The actual quantum source at every bridge](quantum_bridge_cap_source.md),
  SHA256 `6f4d4847218954dc0eff16b2269ada870f36afbaaddd7e1708e8f9e05b5d896f`.

This note uses written proofs only; no mathematical programs or tests
were run.
