# Logarithmic degree after exact Conway source compression

24 November 2026. Research note. Written proof.
Earlier final notes and public manuscripts remain unchanged.

The retained residual vector in the compact reciprocal construction
need not have degree as large as the number of leaves. First compose
the known linear parts of the actual source. Then retain the larger
child at each remaining product. An eliminated continuation halves
its descendant leaf count at every product. This gives a logarithmic
degree bound for the reduced residual, with the original scalar
closing still present.

The construction changes the auxiliary energy and integral, but keeps
the original closed source and the product of its recorded budgets.
It does not estimate that scalar at the hyperbolic volume rate.

## 1. Compress the actual normalized source

Use the full physical packet space \(\mathcal A_N\) and the literal
source of [P], for every \(N\ge2\). Its dimension is \(N\); all
first-normal directions at repeated Casimir roots are included.
Write the original normalized recursion and closing as
\[
 a_v=\Phi_v((a_c)_c),\qquad
             K_N=B_N\,c_Na_{\rm top},\qquad \sigma=\frac1{16}.
 \tag{1}
\]
Here \(B_N\) is the product of all recorded original budgets, including
the original root budget and external scalar convention. Each leaf
constant, unary map, bilinear map and closing row has norm at most
\(\sigma\). Bilinear norms use two separately unit inputs, as in [P].
True normalized packets have norm at most \(\sigma\).

Suppress the unary turns only for counting the product tree. A product
then has zero, one or two inputs coming from another product; an input
not coming from a product is the known transport of an original leaf.
Let \(n_0,n_1,q\) count these three classes. If there is at least one
product, counting the edges of this product tree gives
\[
 n_0+n_1+q=p,\qquad n_1+2q=p-1,\qquad n_0=q+1.
 \tag{2}
\]

Evaluate each zero-product-child vertex at its actual two known
inputs. At a one-product-child vertex, insert its actual fixed other
input. It is now a known complex-linear map on its remaining input.
Compose these maps and the genuine turns along their paths.
The vertices with two product children remain bilinear.
The resulting literal source has
\[
 \ell=q+1\ \hbox{constant leaves},\qquad q\ \hbox{bilinear gates},
 \qquad s_c=2q+1\ \hbox{proper vertices}.
 \tag{3}
\]
Its top linear corridor is composed with the original closing row.
If the original source has no product, take \(q=0\), compose its
unary corridor, and use the same convention of one constant leaf.

This is a composition of the recursion (1), not the Schur-complement
objective of [B]. In particular no minimizer of an earlier auxiliary
energy is substituted for a source packet.

The original budgets are grouped, rather than replaced by estimates
for newly fused unscaled maps. Partition the old vertices into the
bottom constant regions with their outgoing linear corridors, the
bilinear vertices with their outgoing linear corridors, and the top
closing region. Every proper region stops at the next bilinear input;
the corridor above the highest product belongs only to the closing
region. Fixed side-leaf
subtrees belong to the region in which they are inserted. Every old
vertex belongs to exactly one region. The new region budget is the
product of its old budgets; bilinearity makes its normalized map
exactly the corresponding composition of the old normalized maps.
Consequently
\[
 \prod_{\rm regions}b_{\rm region}=B_N,\qquad
 K_N=B_N\,\widetilde c_N\widetilde a_{\rm top}.
 \tag{4}
\]
Every proper region contains an old proper gate or leaf, and the root
region contains the old closing row. All remaining normalized factors
have norm at most one. Thus each new constant, bilinear map and closing
row has norm at most \(\sigma\). This argument keeps every actual
fixed packet, phase, original mark and first normal in its coefficient;
it uses no inverse or cancellation of a fixed packet.

For \(q=0\), the whole proper source has simply become one known
packet. Computing that packet is exact source evaluation, not an
asymptotic estimate for its closing.

## 2. Choose the retained child by leaf count

The following argument applies to any binary packet source with
\(\ell\) constant leaves and no unary vertices, including (3).
For a proper vertex \(v\), let \(\ell(v)\) be its number of descendant
leaves. At every product retain its child with larger \(\ell(v)\);
break ties arbitrarily. The other child is eliminated.
There is one retained packet per product, so the retained vector is
\[
                       u\in\mathbb C^{Nq},\qquad n=Nq .
 \tag{5}
\]
Occurrences are distinct because every proper vertex has one parent.
The top proper packet is always eliminated.

Fix \(u\) and solve the eliminated gate equations exactly, as in [L].
Denote their solution by \(z_0(u)\). A solved leaf is constant.
At a solved product, the larger child is its retained independent
packet and the smaller child is solved recursively. Therefore the
degree \(d(v)\) of its solved value satisfies
\[
 d(v)=0\quad(v\hbox{ a leaf}),\qquad
 d(v)\le1+d(v_{\rm small})
                   \quad(v\hbox{ a product}).
 \tag{6}
\]
After \(h\) such steps, the remaining subtree has at most
\(\ell(v)/2^h\) leaves. Equivalently, induction in (6) gives
\[
                  d(v)\le\lfloor\log_2\ell(v)\rfloor .
 \tag{7}
\]
The estimate is valid for a product whose own output is retained as
well: only its right-hand side is evaluated by this rule.

Let \(F(u)\) be the vector consisting of the retained gate residuals
and the original scalar closing evaluated at \(z_0(u)\). A retained
leaf contributes its prescribed constant minus \(u_v\). A retained
product contributes its right-hand side minus \(u_v\). The closing
is linear in the solved top packet. Hence
\[
 \boxed{\quad
 F:\mathbb C^{Nq}\longrightarrow\mathbb C^{Nq+1},\qquad
 \deg F\le d_\ell:=\max\{1,\lfloor\log_2\ell\rfloor\}.
 \quad}
 \tag{8}
\]
Every component is affine separately in every retained packet slot.
Indeed the retained child at a product is independent of all
variables in the other child's subtree. The tree has no repeated
descendant, so no retained slot is multiplied by itself. Induction
in (6), followed by the affine term \(-u_v\), proves the assertion.
Thus the real polynomial \(\|F(u)\|^2\) has degree at most \(2d_\ell\).
For \(q=1,2\), in particular, \(F\) is affine.

For \(q=0\) no retained variable remains: \(F\) is the scalar
\(\widetilde c_N\widetilde a_{\rm top}\), of degree zero.
The convention \(d_\ell=1\) in (8) is only a harmless uniform bound.
The full lifted energy before elimination still has degree at most
four, independently of this improvement.

## 3. The exact source and compact reciprocal normalization

Apply [C] to this compressed source, multiplying each of its \(s_c\)
proper region budgets and its root budget by \(N\). The new normalized
local maps have norm at most \(\sigma_N=1/(16N)\), and
\[
 \widehat B_N=N^{s_c+1}B_N=N^{2q+2}B_N,\qquad
                     k_N=K_N/\widehat B_N .
 \tag{9}
\]
The rescaling only changes known coefficients, so the degree and
slotwise multiaffinity in (8) are unchanged.
Write \(c_N^{\rm new}=\widetilde c_N/N\) for the rescaled closing.
Write \(a_{\rm leaf}^{\rm new}\) for the rescaled constant leaf packets.
Hereafter \(F\) denotes the residual vector for these rescaled maps.

For clarity, its exact construction is
\[
 r_z=T(u)z+b_z(u),\qquad r_o=C(u)z+b_o(u),\qquad
 T=-I+A_{zz},
\]
\[
 D(u)=C(u)T(u)^{-1},\quad
 F(u)=b_o(u)-C(u)T(u)^{-1}b_z(u),\quad R(u)=I+D(u)D(u)^* .
 \tag{10}
\]
The matrix \(A_{zz}\) is strictly triangular, even for complex
unbounded \(u\), so \(T^{-1}\) is polynomial and \(|\det T|=1\).
No root or first-normal quotient has been taken.
Put \(D_c=Ns_c\), let \(E\) be the sum of all squared rescaled
proper residuals and \(|c_N^{\rm new}x_{\rm top}|^2\), and define
\(\mathcal P_N=(D_c!/\pi^{D_c})\int_{\mathbb C^{D_c}}
E(x)^{-D_c-1}dx\). Exact linear integration gives
\[
 \mathcal P_N=\frac{n!}{\pi^n}\int_{\mathbb C^n}
 \frac{du}{\det R(u)\,[F(u)^*R(u)^{-1}F(u)]^{n+1}} .
 \tag{11}
\]
In particular the determinant is present in the exact full-space
formula. We use [C]'s specified normalization to obtain its compact
unweighted proxy, rather than discard this determinant by assumption.

Let \(\mathcal U_N\) be the product of the \(q\) retained physical
unit packet balls. The compact integral is
\[
 \boxed{\quad
 \mathcal J_N=\frac{(Nq)!}{\pi^{Nq}}\int_{\mathcal U_N}
              \|F(u)\|^{-2(Nq+1)}du,\qquad
             \deg\|F\|^2\le2d_{q+1}.
 \quad}
 \tag{12}
\]
Lebesgue measure is in the chosen physical orthonormal coordinates.
Its dimension, denominator power and factorial are part of the formula.
For every fixed source tree, uniformly over prescribed packets with
the recorded normalized bounds, [C] proves
\[
 |K_N|^2=\frac{\widehat B_N^{\,2}}{\mathcal J_N}
                          (1+O_{\mathscr T}(N^{-1}))
                    \quad(K_N\ne0).
 \tag{13}
\]
This statement is for all sufficiently large levels. At a source
zero, \(\mathcal J_N=+\infty\) and its reciprocal is zero.
When \(q=0\), use the one-point integral:
\(\mathcal J_N=|k_N|^{-2}\), including the same zero convention.
Then the equality in (13) is exact.

To check applicability, the compressed compiler has the same
unique-parent pattern, local arity at most two, closing norm bound
and triangular real Jacobian one as the source in [C].
On the retained unit balls, its proof gives
\(\|D(u)\|\le\sigma_N/(1-\sigma_N)\). Outside those balls the
full residual norm exceeds \(1/4\). These are precisely the two
source-specific inputs in [C]'s determinant and exterior estimates.
All constants depend on the fixed compressed tree and not on a
possibly small nonzero \(K_N\).

## 4. What the degree bound does and does not simplify

The earlier branching result [B] eliminates constant-coefficient
linear response variables from a clamped quartic minimum, retaining
\(2q\) packets and preserving that auxiliary minimum. Here we instead
compose the actual normalized recursion first, then apply the
one-child reduction. This gives \(q\) retained packets and a new
auxiliary energy and integral. Their numerical values are not
identified with those in [B], [L], or the uncompressed [C].
The closed source and the original budget product in (4) are exact.

The logarithmic count in [S] concerns termination of triangular
Newton repairs, via Strahler rank. It does not state (8).
The argument above bounds the degree of the explicitly eliminated
residual vector by choosing which child to retain. No novelty is
claimed for the combinatorial principle that repeated halving gives
a logarithmic bound.

This degree bound must not replace the scalar degree in the
finite-fiber argument. Let \(G\) be the full compressed residual
automorphism and \(f(r)=c_N^{\rm new}(G^{-1}(r))_{\rm top}\)
for the rescaled compiler. Its degree is still at most \(\ell\).
In fact put every internal residual equal to zero and set
\(r_{\rm leaf}=t\,a_{\rm leaf}^{\rm new}\), using the true rescaled leaf
constants. Homogeneity gives the exact restriction
\[
                             f(r(t))=k_N(1-t)^\ell .
 \tag{14}
\]
If \(K_N\ne0\), this proves \(\deg f=\ell\).
Thus (8) concerns the vector after integrating linear packet
variables, not a lower generic degree for the original scalar fibers.

Even when \(F\) is affine, its coefficients contain the complete
actual short components and the prescribed closing row. They can
carry cancellation. The remaining geometric task is an upper
estimate on \(\mathcal J_N/\widehat B_N^2\) with the original cap
retained. The reduced degree, slotwise multiaffinity and compact
domain do not supply that estimate or a finite-exception theorem.
Overlapping contraction networks with shared descendants are
outside the tree argument.

## Complete inputs and closest coverage

The five complete texts were read at matching versions. [P] supplies
the actual full physical source; [L,C] supply exact elimination and
compact calibration; [B,S] identify the closest existing tree
reductions. The compression and degree estimate are proved above.

| Label | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| P | [Physical source compiler](research_conway_uniform_physical_quartic.md) | 477 | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| B | [Branching quartic reduction](research_conway_branching_quartic_source.md) | 267 | f62e3f9fbb1123ee6ad122a3624295172921d626efa9b97e39300ea1806cf2fb |
| L | [One-child linear elimination](research_conway_orthogonal_linear_elimination.md) | 344 | aa53b79685296193d5bf7fc66e53f3a3fbe03fc72a36481fb3aee23afe2ae113 |
| C | [Compact reciprocal source](research_conway_compact_reciprocal_source.md) | 321 | 94f261ac94d20b676cf02c3fb39514ebcb7e2a7c42e114bc5bb0ecb413a7e2b4 |
| S | [Source-visible residual transport](research_conway_source_visible_residual_transport.md) | 420 | 0d344301b0df65246551cf81498eff84582f796a03271b201f8fbba6c7742007 |

Only written mathematics, text reads and metadata operations were used.
No mathematical program, numerical experiment, test, build, git operation,
earlier-final edit, public-manuscript change or ledger edit was made.
