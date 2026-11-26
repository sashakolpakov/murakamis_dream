# Classical gauges for the faithful middle-weight model

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The middle-weight condition has a direct classical meaning in the
actual Gauss coordinates: the product of two based meridians has
upper-left entry one. For every irreducible ordered pair of trace-minus-two
meridians, this is a gauge condition, not an extra condition on its
holonomy. Seven fixed rational charts suffice to choose a regular gauge.

We construct those charts and their frame transitions. Their transitions
form a centralizer-valued cocycle. This is a classical frame torsor;
it is not a scalar torsor of quantum states. No quantum frame operator,
selected source coefficient, or geometric period estimate is inferred.

## 1. The actual Gauss convention and the middle condition

The [shared-meridian calculation](actual_shared_quantum_flags_and_charged_exchange.md)
uses the triangular matrices
\[
 L_+(K,e)=\begin{pmatrix}K&e\\0&1\end{pmatrix},\qquad
 L_-(K,f)=\begin{pmatrix}1&0\\-Kf&K\end{pmatrix}.
\]
In their commutative classical version, with \(K\ne0\),
\[
 G=L_-^{-1}L_+
       =\begin{pmatrix}K&e\\fK&fe+K^{-1}\end{pmatrix}
                          \in\mathrm{SL}_2.             \tag{1}
\]
At the complete main meridian the trace of each such meridian is
\(-2\). An individual trace-minus-two matrix with nonzero upper-left
entry has this unique Gauss decomposition: take \(K=G_{11}\),
\(e=G_{12}\), and \(f=G_{21}/K\).

For the ordered actual meridians use precisely
\[
 A=G_1,\qquad B=L_{-,1}^{-1}G_2L_{-,1},\qquad H=BA.
\]
Then
\[
 H=(L_{-,2}L_{-,1})^{-1}L_{+,2}L_{+,1},\qquad
                         H_{11}=K_1K_2.                 \tag{2}
\]
This is the order appearing in the actual Hurwitz identities; the
product has not been reversed to suit a gauge choice.

The finite [middle-weight model](research_conway_middle_weight_face_model.md)
has physical clocks \(Z,T\), with \(K_i=xZ_i^{-1}\),
\(x=-q^{-1}\), and \(q=e^{\pi i/N}\). On its middle block,
\(ZT=q^{-2}\), so \(K_1K_2=1\) exactly. The corresponding
commutative complete-meridian coordinates have
\[
               K_i=-Z_i^{-1},\qquad Z_1Z_2=1.
                                                               \tag{3}
\]
Thus the classical middle condition is \(H_{11}=1\). This identifies
an algebraic coordinate condition. It does not assert convergence of
the finite matrices to a geometric state.

Throughout the next three sections the entries lie in a field of
characteristic zero; the geometric application is over \(\mathbb C\).

## 2. Seven rational gauges for every irreducible pair

Let \(A,B\in\mathrm{SL}_2\) have trace \(-2\), put
\(H=BA\), and write \(\tau=\operatorname{tr}H\).
Irreducibility means that \(A,B\) have no common invariant line
after extending the coefficient field algebraically.

For these pairs,
\[
                  A,B\text{ irreducible}\quad
                            \Longleftrightarrow\quad \tau\ne2.
                                                               \tag{4}
\]
Indeed, if \(A=-I\), then \(\tau=2\) and the pair is reducible.
Otherwise put \(A=\left(\begin{smallmatrix}-1&1\\0&-1\end{smallmatrix}\right)\)
over the algebraic closure. If \(B_{21}=w\), direct multiplication
gives \(\tau=2+w\). Its vanishing condition \(w=0\) is exactly
that \(B\) preserve the unique invariant line of \(A\).

Assume henceforth \(\tau\ne2\). For a nonzero column \(v\), define
the homogeneous quadratic polynomials
\[
 \begin{split}
 D(v)&=\det(v,Hv),\\
 N(v)&=\det(Av,(H-I)v),\\
 L(v)&=N(v)+D(v)=\det((A+I)v,(H-I)v).
 \end{split}                                                \tag{5}
\]
The letter \(L\) in this section denotes this quadratic polynomial,
not the quantum closing row.

**Lemma 1.** None of \(D,N,L\) is the zero quadratic polynomial.

**Proof.** A two-by-two matrix \(C\) satisfies
\(\det(v,Cv)=0\) for every \(v\) exactly when it is scalar:
evaluate at the two coordinate vectors and their sum. Thus \(D\)
could vanish identically only if \(H\) were scalar. Its only scalar
possibilities in \(\mathrm{SL}_2\) are \(I,-I\).
The first is excluded by \(\tau\ne2\); the second would give
\(B=-A^{-1}\), contradicting \(\operatorname{tr}B=-2\).

Similarly \(N(v)=\det(v,A^{-1}(H-I)v)\). If it vanished
identically, then \(H-I=\lambda A\), whence
\(B=A^{-1}+\lambda I\). Taking traces gives \(\lambda=0\)
and \(H=I\), a contradiction.

Finally \(H-I\) is invertible because
\(\det(H-I)=2-\tau\ne0\). The nonzero matrix \(A+I\)
has rank one. If \(L\) vanished identically, applying the same
scalar criterion after factoring \(H-I\) from the two columns
would make \((H-I)^{-1}(A+I)\) scalar. Its rank is one,
which is impossible for a scalar two-by-two matrix.
\(\square\)

Choose once and for all the seven projective columns
\[
 \mathcal V=\{(1,j)^{\mathsf T}:j=-2,-1,0,1,2,3\}
                                      \cup\{(0,1)^{\mathsf T}\}.
                                                               \tag{6}
\]
For each \(v\in\mathcal V\), use the chart \(D(v)N(v)L(v)\ne0\)
and set
\[
 P_v=[\,v\ \ (H-I)v\,],\qquad
 A_v=P_v^{-1}AP_v,\quad B_v=P_v^{-1}BP_v.                \tag{7}
\]

**Theorem 1.** These seven rational charts cover every pair in (4).
On each chart,
\[
 P_v^{-1}HP_v=H_0(\tau)
      :=\begin{pmatrix}1&\tau-2\\1&\tau-1\end{pmatrix},
 \qquad (A_v)_{11}=N(v)/D(v)\notin\{0,-1\}.             \tag{8}
\]
The actual Gauss decomposition (1)--(2) then has
\[
 K_1K_2=1,\qquad K_i\notin\{0,-1\},\qquad
                         F_{\rm tot}=1,\quad E_{\rm tot}=\tau-2.
                                                               \tag{9}
\]
No eigenvalue extension is needed for these formulas.

**Proof.** Each nonzero homogeneous quadratic has at most two zeros
on the projective line. Lemma 1 therefore leaves at least one of the
seven columns (6) with \(DNL\ne0\).
Also \(\det P_v=D(v)\), and the coordinates of \(Hv\)
in that basis are \((1,1)^{\mathsf T}\). Cayley--Hamilton gives
\(H(H-I)v=(\tau-2)v+(\tau-1)(H-I)v\), proving the first
identity in (8). The determinant formula for a first coordinate
gives its second identity. The exclusions zero and minus one
are precisely \(N\ne0\) and \(N+D\ne0\).

Write \(A_v=L_{-,1}^{-1}L_{+,1}\) using (1), and set
\(G_2=L_{-,1}B_vL_{-,1}^{-1}\). Then
\[
 G_2=L_{-,1}H_0L_{+,1}^{-1},\qquad
                          (G_2)_{11}=1/K_1.
\]
It therefore has its own regular Gauss decomposition, with
\(K_2=K_1^{-1}\notin\{0,-1\}\). This constructs exactly the
actual ordered pair in (2). Multiplication of the triangular factors
gives
\[
 F_{\rm tot}=f_1+K_1^{-1}f_2,\qquad
 E_{\rm tot}=e_1K_2+e_2,
\]
and the product matrix has lower-left entry
\(F_{\rm tot}K_1K_2\) and upper-right entry \(E_{\rm tot}\).
Comparison with (8) proves (9). \(\square\)

The cover is rational over the original coefficient field, including
a rational function field over \(\mathbb Q\). We use projective
frames, so no square root of \(\det P_v\) is required to define
the conjugation. Over \(\mathbb C\) an \(\mathrm{SL}_2\) lift
has the same projective action; its sign is not chosen here as a
quantum normalization.

## 3. Regular physical flag coordinates on this slice

For a trace-minus-two Gauss matrix (1),
\[
                        fe=-\frac{(K+1)^2}{K}.
\]
When \(K\notin\{0,-1\}\), both \(e,f\) are nonzero, and its
unique eigenflag has the finite nonzero coordinate
\[
 s=-\frac{K+1}{e},\qquad
 Z=-K^{-1},\qquad
              f=(1-Z)s,\quad e=\frac{1-Z}{Zs}.           \tag{10}
\]
These are the commutative versions of the actual complete shared-flag
formulas. Apply them to both \(G_i\), and put
\[
                    Z=Z_1,\quad Z_2=Z^{-1},\quad X=-s_2/s_1.
\]
The normalization \(F_{\rm tot}=1\) becomes
\[
               (1-Z)(s_1+s_2)=1,
 \qquad s_1=\frac1{(1-Z)(1-X)},\quad s_2=-Xs_1.          \tag{11}
\]
In particular \(X,Z\ne0,1\). The internal product trace is
\[
 \boxed{\qquad
                  \tau=2+\frac{(1-Z)^2(1-X)^2}{X}.
 \qquad}                                                  \tag{12}
\]
Indeed \(E_{\rm tot}=(Z-1)(s_1^{-1}+s_2^{-1})\), and
\(\tau=2+F_{\rm tot}E_{\rm tot}\).

Conversely, any \(X,Z\ne0,1\), with \(s_i\) given by (11),
defines two matrices through (10), (1), and the ordered prescription
(2). Their product is \(H_0(\tau)\), with (12), and \(\tau\ne2\).
Thus (10)--(12) describe exactly the Gauss-admissible companion slice.

The trace \(\tau\) is also the commutative pair-Casimir symbol:
the [actual pair formula](actual_pair_casimir_commutant_and_rotated_trace.md)
has \(\Omega=F_{\rm tot}E_{\rm tot}+qK_{\rm tot}
+q^{-1}K_{\rm tot}^{-1}\), which becomes the trace of (1)
for the total Gauss matrix. This identifies an internal trace.
It is not the knot's peripheral meridian or longitude eigenvalue
\(M,L\). The \(X,Z\) here are physical flag coordinates, not an
identification with a differently polarized Newton-index clock.

## 4. The frame torsor and its exact overlap cocycle

Fix \(A,B,H\) with \(\tau\ne2\). The full set of projective
frames \(P\) satisfying \(P^{-1}HP=H_0(\tau)\) is a torsor
for the exact matrix centralizer of \(H_0\), modulo scalar matrices:
after one frame is chosen, every other is uniquely obtained by
multiplying it by one element of this quotient group. Scalar multiples
of a frame are identified. Here the fixed trace-minus-two lifts remain
fixed; we do not enlarge the group by allowing conjugation to
\(-H_0\) when \(\tau=0\).

Since \(H_0\) is nonscalar and has a cyclic vector, its entire
invertible matrix centralizer is
\[
 \{aI+bH_0:a^2+\tau ab+b^2\ne0\}.                       \tag{13}
\]
To verify the spanning assertion, a commuting matrix is determined by
its value on a cyclic vector, and that value is a unique linear
combination of the vector and its \(H_0\) image. The determinant
in (13) follows from \(\operatorname{tr}H_0=\tau\) and
\(\det H_0=1\).

For the rational gauges (7), the transition from coordinates \(v\)
to coordinates \(w\) is
\[
 U_{wv}=P_w^{-1}P_v,\qquad U_{wv}H_0=H_0U_{wv},\qquad
                         U_{uw}U_{wv}=U_{uv}.            \tag{14}
\]
This is an exact matrix cocycle, not equality up to a scalar chosen
after evaluation.

For \(\tau^2\ne4\), adjoining a root \(\lambda\) of
\(\lambda+\lambda^{-1}=\tau\) splits the projective centralizer
as a multiplicative one-dimensional torus: the ratio of the two
eigenvalues of \(aI+bH_0\) is
\((a+b\lambda)/(a+b\lambda^{-1})\). Without this extension
the torus need not be split. At \(\tau=\pm2\),
\(H_0=\pm I+N_0\) with \(N_0\ne0\), \(N_0^2=0\).
Modulo scalar matrices its centralizer is \(I+sN_0\), whose
law is addition of \(s\). The value \(\tau=-2\) is allowed
in Theorem 1; \(\tau=2\) is a boundary case discussed below.

The Gauss-admissible frames form only an open subset of this full
torsor, specified by \(K_1\notin\{0,-1\}\). That subset is
nonempty by Theorem 1, but it is not declared invariant under the
entire centralizer. The one-dimensional group in (13)--(14) is a
group of coordinate-frame changes. No action by scalar multiplication
on quantum states has been constructed.

## 5. Markings, turns, and the boundary cases

Conjugate every meridian, based word, and marked flag in the local
configuration by the same \(P_v^{-1}\). All original group relations
and based peripheral words are then conjugated identically. Their
eigenvalues and any already retained logarithmic eigenvalue lifts
are unchanged. Cross-ratios of four marked flags are unchanged too.
Thus geometric ideal shapes and their orientation are preserved by
this local gauge choice. On a chart these transformations are rational,
and hence holomorphic wherever its displayed denominators are nonzero.

For any fixed finite collection of cuts at which the ordered meridian
pairs are irreducible, the seven-chart cover can be applied at each
cut. This gives local regular middle gauges at the actual geometric
representation. It does not supply one simultaneous global frame for
all cuts. If a turn regroups the meridians into a different pair, its
product \(H'\) need not have trace \(\tau\). One must first apply
the actual ordered meridian/flag update and then use a chart for \(H'\).
The same-product centralizer formula (14) alone does not describe this
regrouping. The actual finite turn remains the independently proved
linear packet operation in the middle-weight model.

There are necessary boundary cases. A reducible trace-minus-two pair
has \(\tau=2\). If its product is the identity, then
\(B=A^{-1}\), the condition \(K_1K_2=1\) is automatic wherever
the Gauss factors exist, and \(P_v\) in (7) is singular for every
\(v\). This includes the ordinary inverse-pair cap configuration.
Its frame group is the full projective linear group, and it has no
companion frame of the form (8). If the product is a nonidentity unipotent matrix, a companion
frame still exists, but the regular flag chart of Section 3 fails:
in \(H_0(2)\) coordinates the trace conditions give
\((A_v)_{12}=0\) and \((A_v)_{11}=-1\).
These are cap or boundary charts, not cases that can be deleted from
the finite-exception target. A globally irreducible hyperbolic
representation does not by itself assert irreducibility of every
chosen two-meridian subgroup.

The theorem concerns ordinary group equations and their marked
geometric solutions. It shows that the regular middle clock relation
is not an additional local restriction on an irreducible pair.
It does not identify a geometric solution with a selected finite-source
saddle, construct a quantum lift of \(P_v\), prove bounded norms for
such a lift, or preserve a quantum coefficient merely by conjugating
classical flags. The actual full coefficient cycles, first-normal
directions, and marked closing still need their own source-preserving
transport. No positive face atlas, Rivin-contour pushforward, or new
volume identity is proved here.

## Complete direct sources

All three complete matching texts were read. They fix the actual Gauss
ordering, pair Casimir, and faithful middle representation. The
rational cover, gauge construction, regular flag chart, and centralizer
cocycle are proved above.

| Source | SHA-256 |
|---|---|
| [Actual shared meridians and Gauss flags](actual_shared_quantum_flags_and_charged_exchange.md) | dcab795cc141e2e1db726998cf7b1141dd03c681eaae9076387f90581f53a7d9 |
| [Actual pair Casimir and marked source](actual_pair_casimir_commutant_and_rotated_trace.md) | 00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666 |
| [Faithful middle-weight model](research_conway_middle_weight_face_model.md) | 1813a5ec78bda1df746e53227bc3d9e36c4b3d230bd648a10537a387db87ebac |

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation,
or edit to a previous final was performed.
