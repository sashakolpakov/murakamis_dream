# An exact pinned Green formula for the unit coherent source

22 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

The full product of two unit coherent inputs solves an explicit
positive tridiagonal system with condition number at most \(6N^2\).
Its forcing has only two coordinates, both known finite products.
The same system gives an exact formula for any original exterior,
including one whose scalar observation is small or zero. No
approximate eigenvector or unknown closed invariant is used.

The proof uses only the algebra and two-crossing profile in Sections
1--3 of the
[unit-source theorem](research_unit_coherent_product_source_gap.md).
It does not use that theorem's geometric exponential estimate or
its approximate lowest-eigenline construction. A general directed-path
argument controls all coordinates, including every exact zero block.

## 1. The literal full-source data

Let \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(\kappa=e^{\pi i d^2/(2N)}\). Work in the full \(N\)-dimensional
Newton coefficient space with orthonormal basis \(e_0,\ldots,e_d\).
All repeated-root derivative coordinates are retained. This norm is
not the uniform physical Hilbert--Schmidt norm. Write
\(f_0,\ldots,f_d\) for the inherited centered orthonormal basis.

Fix a compact subset \(K\) of
\[
 b>0,\qquad c>0,\qquad b+c<1,\qquad
 y=-e^{-2\pi ib},\quad z=-e^{-2\pi ic}.
 \tag{1}
\]
The original normalized coherent product is
\[
 w=u_N(y)u_N(z)=\sum_{j=0}^d b_je_j,\qquad
 u_N(t)=N^{-1/2}\sum_{a=0}^dt^af_a\quad(|t|=1).
 \tag{2}
\]
Its exact coefficients, including every source resonance, are
\[
 b_j=\frac{\kappa^2(-q)^j}{N^2}
 (Q;Q)_j(Qyz;Q)_j
 (-qQ^{j+1}y;Q)_{d-j}(-qQ^{j+1}z;Q)_{d-j}.
 \tag{3}
\]
Here \((a;Q)_m=\prod_{r=0}^{m-1}(1-aQ^r)\). This is a
polynomial formula, with no limiting \(0/0\).

For \(0\le j<d\), define
\[
 a_j=(1+qQ^{j+1}y)(1+qQ^{j+1}z),\quad
 n_j=-q(1-Q^{j+1})(1-yzQ^{j+1}),\quad
 \nu_j=(|a_j|^2+|n_j|^2)^{1/2},
 \tag{4}
\]
\[
                    (Ax)_j=(a_jx_{j+1}-n_jx_j)/\nu_j .
 \tag{5}
\]
Uniformly on \(K\), for all sufficiently large \(N\), the
\(\nu_j\) have a positive lower bound, \(Aw=0\), and
\(\|A\|^2\le2\).

Let \(u_+^N\) be the upper of the two roots in one period of
\[
 |(1-v)(1-yzv)|^2-|(1+qyv)(1+qzv)|^2=0,\qquad
 v=e^{2\pi iu},
 \tag{6}
\]
and put \(k=\lfloor Nu_+^N\rfloor\). The unit-source theorem
proves \(1\le k<d\) for large \(N\). The expression on the
left of (6) is negative outside its two simple roots and positive
between them, with uniform strict margins from \(0,1\).
Exact grid ties are permitted.

## 2. A directed-path coercivity lemma

First consider any complex adjacent-coordinate rows of the form (5),
with \(\nu_j>0\). Direct edge \(j\) forward, from \(j\) to
\(j+1\), if \(|n_j|<|a_j|\), and backward otherwise. Equality
is assigned backward throughout. Let \(\mathcal P\) be the set
of vertices with no incoming edge, and put
\[
 P_{\mathcal P}=\sum_{p\in\mathcal P}|e_p\rangle\langle e_p|,
 \qquad T_{\mathcal P}=A^*A+P_{\mathcal P}.
 \tag{7}
\]
Then, without a source, support or root hypothesis,
\[
 \boxed{\qquad \frac1{2N^2}I\le T_{\mathcal P}\le3I .\qquad}
 \tag{8}
\]

Indeed the orientation chooses the stable recurrence direction:
\[
 \begin{array}{ll}
 |x_{j+1}|\le|x_j|+\sqrt2|(Ax)_j|,& j\longrightarrow j+1,\\
 |x_j|\le|x_{j+1}|+\sqrt2|(Ax)_j|,& j+1\longrightarrow j .
 \end{array}
 \tag{9}
\]
The normalized coefficient used as divisor has modulus at least
\(1/\sqrt2\), and the preceding-coordinate coefficient has
modulus at most one. The inequalities remain valid when one of
\(a_j,n_j\) vanishes.

An oriented path has no directed cycle. Tracing incoming edges
backwards finds a directed path from some \(p\in\mathcal P\)
to each vertex \(i\), of length at most \(N-1\). Iterating (9)
and applying Cauchy--Schwarz gives
\[
 |x_i|^2\le(2N-1)
       \left(|x_p|^2+\sum_{j\ {\rm on\ path}}|(Ax)_j|^2\right)
       \le(2N-1)\langle x,T_{\mathcal P}x\rangle .
 \tag{10}
\]
Sum over the \(N\) vertices to prove the lower bound in (8).
Each normalized row has norm one and adjacent support, so
\(\|A\|^2\le2\); also \(P_{\mathcal P}\le I\). This proves
the upper bound, with every zero coordinate still present.

There is a finite-degree forcing consequence. Suppose the rows
sample one period in increasing order and
\(|n|^2-|a|^2\) is a nonzero real trigonometric polynomial of
degree at most \(m\). Each interior directed source requires a
sample transition from a nonnegative value to a negative one.
Distinct such transitions give distinct root intervals; there
are at most \(2m\) roots in one period. Thus the safe bound
\(|\mathcal P|\le2m+2\) holds, including both endpoints.
If that polynomial is identically zero, the specified orientation
is entirely backward and has just one source. Any actual vector
in \(\ker A\) is therefore reconstructed from a bounded number
of its coefficients when this degree is bounded. This does not
assert any new Conway recurrence.

For (4), the finite two-crossing sign pattern gives exactly the
directed sources \(0,k\). At an exact upper grid root, the
backward equality convention selects \(k\), rather than \(k-1\).
Thus define
\[
                         T=A^*A+P_0+P_k .
 \tag{11}
\]
It obeys (8), so its condition number is at most \(6N^2\).
Only local coefficients and the fixed-degree root selection (6)
are used, without a reset or source support classification.

Since \(Aw=0\), the exact full source satisfies
\[
 \boxed{\quad
       Tw=f,\qquad f=b_0e_0+b_ke_k,\qquad w=T^{-1}f .
 \quad}
 \tag{12}
\]
Both forcing coefficients are known by (3); \(b_0\) may vanish.
There is no division by the original scalar, by \(b_0\), or by
a packet norm. Unlike a lowest-eigenline approximation, (12)
has no transverse error. Equivalently, \(w\) is the unique
minimizer, of minimum zero, of the unconstrained positive quadratic
\[
                \mathcal Q(x)=\|Ax\|^2+|x_0-b_0|^2+|x_k-b_k|^2 .
 \tag{13}
\]
Its normal equation is precisely \(Tx=f\). This zero minimum
is not the global Conway quartic minimum encoding a closed scalar.

## 3. Arbitrary original gluing and its co-source energy

Let \(\ell\) be any specified complex-linear exterior row, in
the original phase convention, and solve
\[
                              Tz=\ell^* .
 \tag{14}
\]
Hermitian symmetry proves
\[
 \boxed{\quad
           \ell w=z^*f=\overline{z_0}b_0+\overline{z_k}b_k .
 \quad}
 \tag{15}
\]
An actual further component can supply \(\ell\); the identity
does not require its dual norm to be polynomial.

For example, if \(v=\sum_jv_je_j\) is the actual other packet,
the original Frobenius pairing is
\(\phi(vw)=\sum_jv_{d-j}b_j\). Thus (14) has right side
\(J\overline v\), where \(Je_j=e_{d-j}\) and the bar denotes
coefficient conjugation. Formula (15) evaluates precisely that
bilinear gluing, with no Hermitian replacement. For a turned
output \(Jw\), replace \(T,f\) by \(JTJ,Jf\); the original
unitary involution preserves (8).

For any trial \(x\), put \(r=f-Tx\), and write \(G=T^{-1}\).
Then
\[
 \ell w-\ell x=z^*r,\qquad
 |\ell w-\ell x|^2\le(\ell G\ell^*)(r^*Gr).
 \tag{16}
\]
This is Cauchy--Schwarz for \(T^{1/2}z,T^{-1/2}r\).
Both factors are positive quadratic forms obtained from the
specified source and exterior. The elementary bounds are
\[
 \ell G\ell^*\le2N^2\|\ell\|^2,\qquad
                         r^*Gr\le2N^2\|r\|^2 .
 \tag{17}
\]
There is also a dual-trial bound with a known source scale.
For any \(\widetilde z\), put \(s=\ell^*-T\widetilde z\).
Then
\[
 \ell w-\widetilde z^*f=s^*w,\qquad
 |\ell w-\widetilde z^*f|^2
       \le (|b_0|^2+|b_k|^2)(s^*Gs).
 \tag{18}
\]
Cauchy--Schwarz in the \(T\)-energy proves this because
\[
                       w^*Tw=f^*Gf=|b_0|^2+|b_k|^2 .
 \tag{19}
\]
No unknown packet norm or original closed scalar enters its scale.

One may retain the coherent scalar \(z^*r\) itself instead of
bounding it. Adjoint-weighted residual estimation is standard.
The source-specific result here is the exact system (12) and
its uniform polynomial conditioning, not a new general duality
principle.

## 4. A scalar Green formula retains every block and phase

Write \(t_j=T_{jj}\) and \(h_j=T_{j,j+1}\). Formula (5) gives
\[
 h_j=-\overline{n_j}a_j/\nu_j^2,\qquad
 t_j=\frac{|a_{j-1}|^2}{\nu_{j-1}^2}
       +\frac{|n_j|^2}{\nu_j^2}
       +{\bf1}_{j=0}+{\bf1}_{j=k},
 \tag{20}
\]
with absent boundary terms omitted. Define leading and trailing
principal determinants by the continuant recurrences
\[
 D_0=1,\quad D_1=t_0,\quad
 D_{r+1}=t_rD_r-|h_{r-1}|^2D_{r-1},
 \tag{21}
\]
\[
 E_N=1,\quad E_{N-1}=t_{N-1},\quad
 E_r=t_rE_{r+1}-|h_r|^2E_{r+2}.
 \tag{22}
\]
All are strictly positive by (8). For \(i\le j\),
\[
 G_{ij}=
 \frac{(-1)^{j-i}h_i\cdots h_{j-1}D_iE_{j+1}}{D_N},
 \qquad G_{ji}=\overline{G_{ij}}.
 \tag{23}
\]
The empty product is one. Expanding principal determinants
proves (21)--(22). In the cofactor for \(G_{ij}\), the unique
chain joining \(i\) to \(j\) contributes \(h_i\cdots h_{j-1}\).
Its removal leaves the two principal blocks with determinants
\(D_i,E_{j+1}\), and its cofactor sign is \((-1)^{j-i}\).
This proves (23). A vanishing offdiagonal makes this product
zero across the actual block boundary, without deleting a
coordinate or taking a singular limit.

There is an elementary path-gauge positivity statement. Choose a
diagonal unitary \(V\), recursively on each nonzero offdiagonal
block, so that \(V^*TV\) has offdiagonal entries \(-|h_j|\).
Then \(3I-V^*TV\) is entrywise nonnegative, with spectrum in
\([0,3-(2N^2)^{-1}]\). Its convergent Neumann series proves
that \(V^*GV\) is entrywise nonnegative. This is only the
transformed Green kernel: both \(V^*f\) and \(\ell V\) remain
in (15). It does not make an arbitrary original closing positive.

## 5. Scope and complete proof source

This replaces a local approximate spectral construction by an
exact linear solve and gives source-visible error control for
any specified exterior. It constructs the same full product,
not a scalar surrogate. It does not remove cancellation in
(15), bound an arbitrary co-source energy at a geometric
action, or establish further binary closure. Arbitrary short
fillings and the finite-exception volume theorem remain open.

The sole complete direct proof source is the 467-line
[unit coherent-product source theorem](research_unit_coherent_product_source_gap.md),
SHA-256
cb5d4e0af1b74f2e6740d2ecced5356666f24a6f59067e6a669f889adb5b9277.
Its entire matching text was read. Only its algebraic source and
two-crossing statements are used, not its geometric scalar lower
bound. The directed-path conditioning estimate, exact
forcing, original co-source pairing and Green formulas are
proved above. Only written mathematics and text operations
were used.
