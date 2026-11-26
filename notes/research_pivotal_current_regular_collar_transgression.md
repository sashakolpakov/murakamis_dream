# The actual pivotal current on a regular geometric collar

Private written proof, 18 November 2026.

The unilateral closing current has an exact finite-difference
representative in the original occupation source. On a holomorphic
translation prism this difference is an exterior derivative. Its
normal reduction on a fixed regular geometric collar is of order
\(h\), with explicit tangential endpoints and normal side currents.
The exterior \(N\)-scale pivotal factor does not create an additional
\(N\) on such a collar.

The original cut, tail pivots, finite support and parameter-normal
walls remain. No original cycle is placed in a descending collar,
and no singular endpoint packet is estimated. The complete proof
directs are R, E, C and U, pinned below.

## 1. An external-head primitive coordinate system

Let the knot braid have \(b\ge2\) strands and \(c\) crossings, and
put \(m=c+1\). Choose a pivotal tail head \(j\ne1\); the original
cut stays on head 1. Put
\[
 d=N-1,\qquad h=2\pi i/N,\qquad q=e^{h/2},\qquad Q=e^h.
 \tag{1}
\]
R gives the actual matching lattice and its physical support.
Label strands by their input positions and follow them through
the braid. If \(a\in\mathbb Z^b\) denotes initial occupations and
\(n\in\mathbb Z^c\) denotes transfers, the final occupations are
\[
                              Pa+Dn.
 \tag{2}
\]
Here \(P\) is the permutation and each column of \(D\), in output
strand labels, is a signed difference of two coordinate vectors.
The graph of these columns is connected: otherwise every crossing
preserves its disconnected parts, whereas \(P\) is one cycle.

Choose a spanning tree of that graph. Its \(b-1\) columns map
their integer coefficients bijectively to the integer vectors
of coordinate sum zero. Remove a tree leaf successively: its
equation determines its incident coefficient integrally, and
the last equation is the zero-sum condition. Thus the trace rows
\[
                             Dn=(I-P)a
 \tag{3}
\]
determine the tree transfers integrally from all \(b\) initial
occupations and the \(c-b+1\) non-tree transfers. Those entries
are primitive coordinates on the whole matching lattice; their
inverse simply reads them from the reconstructed state. Their
change from R's coordinates is therefore unimodular.

Let \(v\) increase \(a_j\) by one, fixing the other initial
occupations and the non-tree transfers. In R's coordinates
it is a fixed integer vector, with
\[
              a_j(v)=1,\qquad a_i(v)=0\quad(i\ne j).
 \tag{4}
\]
All changed tree transfers remain. The original cut and all
other tail pivots are unchanged by this reindexing. It is not
a common shift of every occupation.

Write \(S_N\subset\mathbb Z^m\) for the exact physical support.
An array value outside \(S_N\) is zero. This finite zero extension
is not an analytic continuation or a negative factorial value.

## 2. Exact rows before root specialization or differentiation

In this section \(q,M\ne0\) are independent finite-array parameters.
Keep C's ADO pivot \(g=K^{1-N}\), the original diagonal cut,
scalar line and word \(W\). On the chosen tail,
\[
 g_a=g_0\omega^a,\qquad \omega=Q^{N-1},\qquad
 Q_{\rm f}=-q^{-1}S_-,\qquad
 F e_a=(1-Q^{a+1})e_{a+1}\quad(a<d).
 \tag{5}
\]
The cut here may be the highest projector or E's specified
normalized complex-binomial diagonal cut: both commute with
the chosen tail matrices. The identity below keeps whichever
cut was chosen, including all of its marked defects. Equality
of their unmarked scalar values is not equality of marked sources.
The missing arrows are zero. Let \(f_a\) be the actual diagonal
contraction at tail occupation \(a\), including its pivot and
all the other source factors. Matrix multiplication gives the
output-row current
\[
 J_a=q^{-1}(1-Q^a)\{f_a-\omega f_{a-1}\},
                   \qquad 0\le a\le d,\quad f_{-1}=0.
 \tag{6}
\]
The term \(FWQ_{\rm f}\) uses \(W\)'s diagonal at \(a-1\);
the term \(FQ_{\rm f}W\) uses it at \(a\). No intertwining or
replacement of the marked trace is used.

Set
\[
 b_a=q^{-1}\omega(1-Q^{a+1}),\qquad
 \lambda_a=q^{-1}(1-\omega)+q^{-1}Q^a(\omega Q-1).
 \tag{7}
\]
Then \(q^{-1}(1-Q^a)-b_a=\lambda_a\). For every output test,
\[
\begin{split}
 \sum_{a=0}^{d}\chi_aJ_a
 ={}&\sum_{a=0}^{d}\lambda_a\chi_af_a
       -\sum_{a=0}^{d-1}b_a(\chi_{a+1}-\chi_a)f_a\\
    &+b_d\chi_df_d,\qquad b_d=q^{-1}\omega(1-Q^N).
\end{split}
 \tag{8}
\]
This is exact finite summation, with no difference replaced by
a derivative. At a physical root it becomes
\[
 \lambda_a=\lambda_h=\rho/Q,\quad \rho=q-q^{-1},\qquad
 b_a=q^{-3}(1-Q^{a+1}),\quad b_d=0.
 \tag{9}
\]
In particular a proper interval retains the endpoint flux
\[
 \sum_{a=L}^{R}J_a=\lambda_h\sum_{a=L}^{R}f_a
                           +b_Rf_R-b_{L-1}f_{L-1}.
 \tag{10}
\]
Only the missing bottom term and the physical root top term
vanish at the full interval endpoints.

Equation (8) precedes all parameter derivatives. They hit
\(\omega\), \(1-Q^N\), the cut, pivots, scalar line and the
whole word. The top term erased in (9) has nonzero quantum
normals. As in C, restriction to \(M=-q^N\) keeps the whole
chain rule but does not alone replace this closed ADO pivotal
germ by an ordinary colored-Jones pivotal/twist germ.

## 3. A recorded interpolation of the actual current array

Return to (1). Let \(I_N^0(k)\) be the zero-extended original
summand, with its fixed integer Fourier character as in R.
Using Section 1, label the first term of (6) by \(k-v\) and
the second by \(k\). This is an explicit reindexing of the
current's affine matching equations. The first term's output
tail occupation is one above its \(W\) occupation; its other
external occupations stay fixed. No transfer is removed.

Put \(B_N^0(k)=b_{a_j(k)}I_N^0(k)\). The whole current array
has the exact representative
\[
 {\cal J}_N^0(k)=\lambda_hI_N^0(k)
                              +B_N^0(k)-B_N^0(k-v).
 \tag{11}
\]
The would-be output \(a_j=N\) vanishes by \(b_d=0\).
The other support faces remain in the zero-extended arrays.
Summing (11) gives C's exact root identity
\[
                  \Phi(F[W,Q_{\rm f}])=\lambda_h\Phi(W).
 \tag{12}
\]
For any finite state test,
\[
 \sum_k\chi(k){\cal J}_N^0(k)
 =\lambda_h\sum_k\chi(k)I_N^0(k)
       -\sum_k\{\chi(k+v)-\chi(k)\}B_N^0(k).
 \tag{13}
\]
Thus a set and its translate have a specified interface current.
Counting its states gives no estimate of their weighted sum.

Let \(\zeta=hk\), and let \(\omega_N\) be a specified literal
Fourier summand's top holomorphic form, including its original
measure and scalar line. Define
\[
 \begin{split}
 u_j&=a_j(\zeta),\qquad b_N=q^{-3}(1-e^{u_j+h}),\\
 \beta_N&=b_N\omega_N,\qquad T_\xi(\zeta)=\zeta-\xi hv
                                  \quad(0\le\xi\le1).
 \end{split}
 \tag{14}
\]
The recorded analytic representative of (11) is
\[
                {\cal J}_N=\lambda_h\omega_N+
                                         \beta_N-T_1^*\beta_N.
 \tag{15}
\]
It interpolates the literal current array with that reindexing.
This is not equality of arbitrary off-lattice interpolants.
Integer Fourier characters are periodic under the integer
shift, as is a retained cotangent kernel wherever holomorphic.

On a compact regular slit chart all factorial lengths and their
\(O(h)\) shifts remain in the same holomorphic domain for large
\(N\), by R. Formula (15) is used on a chain only when its
entire translation prism lies there. Otherwise the additional
source or pole currents have not been supplied by this argument.

## 4. Exact translation and normal-coarea transgression

On that prism set
\[
             {\cal B}_N=\int_0^1T_\xi^*(\iota_v\beta_N)\,d\xi .
 \tag{16}
\]
Holomorphic top forms are closed, and
\(\partial_\xi T_\xi^*\beta_N=-h\,dT_\xi^*(\iota_v\beta_N)\).
Hence
\[
 \boxed{\qquad {\cal J}_N=\lambda_h\omega_N+h\,d{\cal B}_N.\qquad}
 \tag{17}
\]
For a compact oriented real \(m\)-chain with all its faces,
\[
 \int_\Gamma{\cal J}_N
      =\lambda_h\int_\Gamma\omega_N
                              +h\int_{\partial\Gamma}{\cal B}_N .
 \tag{18}
\]
The sign is positive. Internal faces cancel only when present
with opposite orientations in the specified chain.

Take normal collar coordinates \((t,y_1,\ldots,y_c)\), with
orientation \(dt\wedge dy\), and a fixed normal chain \(D\). Put
\[
 \begin{split}
 {\cal W}_N(t)&=\int_D\omega_N,\qquad
 {\cal L}_N(t)=\int_D{\cal J}_N,\\
 K_N(t)&=\int_D{\cal B}_N|_{\{t\}\times D},\\
 {\cal E}_N(t)&=-dt\int_{\partial D}\iota_{\partial_t}{\cal B}_N.
 \end{split}
 \tag{19}
\]
The first two are one-forms and \(K_N\) is a function.
Writing \({\cal B}_N=B_0dy+dt\wedge\gamma\) proves
\[
 \boxed{\qquad
 {\cal L}_N=\lambda_h{\cal W}_N+h\,dK_N+h\,{\cal E}_N .
 \qquad}
 \tag{20}
\]
Indeed \(d{\cal B}_N=dt\wedge(\partial_tB_0dy-d_y\gamma)\).
Thus both tangential endpoint values and the normal side
integral remain. For a moving normal chain, pull back its full
parametrization first: its derivatives and moving boundary
enter (19); no derivative of the chain is discarded.

## 5. The geometric leading current

Assume exactly E's positive-certificate regular chart, its
Fourier charge and transported Gaussian orientation. Its phase
has \(c\) nondegenerate normals and one critical framing
coordinate. U's bounded degree-zero mark has principal function
\[
                                t=r/s_\theta
 \tag{21}
\]
on this critical curve and its common-momentum orbit.
In this section and Section 6 the source is specifically E's
complex-binomial-cut source, with its full cut weight, pivots,
scalar line and marks. Sections 2--4 apply to that same source
without replacing it by the highest-cut marked source.

Use its recorded principal extension on the regular literal
phase chart, and keep this function as base coordinate.
It is a submersion along the critical curve. Taylor expansion
in the other coordinates and the analytic symmetric square
root of the invertible normal Hessian give a holomorphic
normal form preserving \(t\).

For precision this principal extension may be obtained directly
from the finite insertion: expand its finitely many bounded
shifts in the original factorial array, retain their original
coefficients, and take their leading ratios on the buffered
literal chart. Taylor expansion of the phase gives the
generating-correspondence symbol. U identifies its restriction
with (21). E's derivative bounds justify these fixed shifts.
The same construction applies to any fixed polynomial of the
mark; it does not justify an unrestricted growing marked word.

Let \(C_\beta\,dt\) be E's constant nonzero leading one-form and
put, with exactly E's original scalar convention,
\[
 {\cal N}_N=E_NN^{1/2}(2\pi)^{c/2}c_0^{c/2-m}e^{\Phi_*/h},
                              \qquad c_0=2\pi i.
 \tag{22}
\]
Fix a compact \(t\)-arc and a fixed descending normal ball
with strict Gaussian margin. Then
\[
                   {\cal W}_N={\cal N}_N\{C_\beta+O(h)\}\,dt.
 \tag{23}
\]
All fixed chart derivatives are uniform. Define
\[
                \eta_j(t)=(1-A_j(t))\,(vt)|_{\rm crit},
                                      \qquad A_j=e^{u_j}.
 \tag{24}
\]
This uses the chosen principal extension, not an arbitrary
identification of \(v\) with the centralizer vector.

Contraction in (16) and the same normal Gaussian give
\[
                    K_N={\cal N}_N\{C_\beta\eta_j(t)+O(h)\}.
 \tag{25}
\]
The displacement in (16) is \(O(h)\), whereas the Gaussian
width is \(O(\sqrt h)\). Its phase displacement at the critical
point is \(O(h^2)\), giving \(O(h)\) in the exponent. The normal
contour translates by this small amount with its side retained;
odd normal Taylor terms integrate to zero. E's Taylor estimates
therefore prove (25), including fixed \(t\)-derivatives.

The fixed normal side retains a strict Gaussian margin after
translation, so \({\cal E}_N/{\cal N}_N\) is exponentially small
up to a fixed polynomial power. As \(\lambda_h=h+O(h^2)\),
\[
 \boxed{\quad
 {\cal L}_N=h{\cal N}_NC_\beta\,d\{t+\eta_j(t)\}
          +O(h^2{\cal N}_N)\,dt+h{\cal E}_N .
 \quad}
 \tag{26}
\]
No identity \(\eta_j'=-1\) is assumed. Computing that coefficient
requires the actual principal extension in (24); the trace row
alone does not determine it. A different normal fibration can
change the displayed primitive and must change its side currents
consistently. At finite \(N\) the exact formula is (20), not a
claim that every higher-order reduced density is constant.

## 6. The remaining endpoint problem

On the specified bounded regular collar, including finite
tangential endpoints, the current is \(O(h{\cal N}_N)\).
C's factor \(Q/\rho\) restores the original \(O({\cal N}_N)\)
scale. It supplies no extra \(N\) on this local block.

For a test changing by order one in a single lattice layer,
the difference in (13) is order one, not \(O(h)\). Formula
(26) does not estimate that source pairing near a factorial
wall, a degenerating normal Hessian or an unbounded framing
end. Nor does it estimate the full normal derivatives of
the top term in (8). These are explicit retained terms.
No magnitude, sign or nonvanishing of an endpoint packet
is inferred from the boundedness of the unilateral coupon.

In particular finitely many bounded-mass regular blocks of
the \(N^{1/2}\) type (22), with a smaller remainder, cannot
exhaust a source known to have an \(N^{3/2}\) leading scalar.
The present formula identifies the exact interface/coarea
terms a proposed exhaustion would still have to control.
It neither selects such an endpoint mechanism nor assigns
a period one to the residual coordinate.

R's physical band, mixed facets, translated sides, other
Fourier aliases and framing-exception strata remain. The
new comparison is valid on supplied whole translation prisms.
It is not an original framing pushforward or a nonzero
geometric coefficient.

## Complete proof-source pins

* R: notes/research_actual_oblique_geometric_contour_decomposition.md,
  SHA256 9180de472bafb38c479d3e1aafac6c75c388d668371892f54219de658728034c.
* E: notes/research_soft_cut_morse_bott_density.md,
  SHA256 e411f25c7b66b61d865427db1e1f789aeb09b9c76471a303dfdb8d7673fe6f9a.
* C: notes/research_routed_residue_cut_current_adapter.md,
  SHA256 f6e634b156ac6f208083243fae6137dc712a25965f5fd77b713bb7b55d21291d.
* U: notes/research_actual_unilateral_flag_jacobi_current.md,
  SHA256 96b2fb080df630b52927063250965f2ef25a3e06e6457db9430620f31d22240c.

All four complete texts were freshly read nontruncated in this
active author sequence. Their actual support, normalizations,
current identities, coordinate scope and Gaussian premises
were checked. Only written mathematics and text/hash operations
were used. Frozen and public files were not changed.
