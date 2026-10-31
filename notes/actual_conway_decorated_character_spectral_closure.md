# Controlling a turn preceded by an actual character operator

A polynomial operator in a knot calculation is determined at a repeated spectral node by both its value and its first derivative. This note uses a norm retaining both pieces of data. It proves that a specific physical operation preserves useful bounds in that norm: multiply by the actual circle character and retained half twist, then apply the physical turn.

The result has three parts. The operation adds a precisely determined exponential cost, concentrates the canonical output polynomial near the spectral point \(-2\), and gives a strict loss when any original circle color is a fixed fraction away from complete. Products preserve the same kind of estimate. Consequently one can iterate these operations through the recursive class defined in Section 4. The [reduced-hub source adapter](actual_conway_reduced_hub_source_normal_form.md) identifies that class with trees in which every multiplication hub has a distinguished original character.

A turn without such a character is a different operation. Its sharp norm cost is computed in Section 5, but this cost cannot simply be added to a previously fixed geometric action. The later [positive-probe theorem](actual_conway_unflagged_core_probe_bound.md) supplies the additional estimate used for those regions in the full strict-tree proof.

The finite inputs are the [original positive Newton turn and pairing](actual_newton_turn_positive_gram.md),
the [full-Hermite localization estimates](actual_conway_root_star_full_jet_localization.md),
and the [exact root-character Fourier theorem](actual_conway_root_character_fourier_contraction.md).
The [rigid-spine geometry](actual_conway_rigid_spine_and_flagged_tree_geometry.md)
separately identifies the complete action for the fully flagged class.

## 1. A norm that retains the full spectral data

Fix the level \(N\), set \(d=N-1\) and \(M=\lfloor d/2\rfloor\), and use the following polynomial and basis. Here \(T_N\) is the Chebyshev polynomial of the first kind; the physical turn is the separate map \(T\) in (1).
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 c_k=2\cos((2k+1)\pi/N),\qquad
 \widehat B_r(z)=\frac{\prod_{a<r}(c_a-z)}{s_r^2},
 \qquad s_r=\prod_{a=1}^r2\sin(\pi a/N),\quad s_0=1.
\]
The algebra is \(\mathbb C[z]/(P_N)\). The roots of \(P_N\) are the actual Casimir nodes: they are double except for the simple node \(-2\) at odd levels. The basis elements \(\widehat B_r\) have indices \(0\le r\le d\). The marked closure functional \(\phi\) and the physical turn obey
\[
 T\widehat B_r=\widehat B_{d-r},\qquad
 \phi(\widehat B_r\widehat B_t)=\mathbf1_{r+t=d}.
 \tag{1}
\]
At a double node \(c\), reduction modulo \((z-c)^2\) retains \(F(c)+F'(c)(z-c)\). For example, the local class \(z-c\) has zero value and nonzero derivative, so nodal values alone would not detect it. The following faithful norm measures exactly the retained Hermite data:
\[
 \|F\|_{\mathcal J}
 =\max\{\max_{\text{double }c}(|F(c)|+|F'(c)|),
                    |F(-2)|\text{ if }N\text{ is odd}\}.
 \tag{2}
\]
The derivative rule \((FG)'=F'G+FG'\) shows that this norm is submultiplicative. Let \(R\) be the original crossing operator, and let \(L_j(z)=(-1)^{j-1}U_{j-1}(z/2)\) be the color-\(j\) circle character, where \(U_{j-1}\) is the second-kind Chebyshev polynomial. The physical color satisfies \(1\le j\le N\), and \(\epsilon\in\{0,\pm1\}\) records the retained half twist. The residue formula and the actual crossing data give
\[
 |\phi(F)|\le3N\|F\|_{\mathcal J},\qquad
 \|R^\epsilon L_j\|_{\mathcal J}\le CN^3
 \quad(1\le j\le N,\ \epsilon=0,\pm1).
 \tag{3}
\]
The second inequality is for the actual crossing, not a semisimple
replacement: its node values have modulus one,
\[
 \frac{R'(c_k)}{R(c_k)}
 =-\frac{N-1-2k}{4i\sin((2k+1)\pi/N)}
\]
at every double node, and this has size \(O(N^2)\). The original circle is
\(L_j(z)=(-1)^{j-1}U_{j-1}(z/2)\); it has
\(|L_j|\le N\), \(|L_j'|\le CN^3\) on \([-2,2]\).
The odd simple node has no derivative obligation.

The input \(E_N\) may already be a product of subtree operators. It may have degree greater than \(N-1\) before reduction. The operation studied here, called a decorated character turn, is
\[
 D_{N,j}^{\epsilon}[E_N]
       =T(R^\epsilon L_jE_N)\pmod {P_N}.
 \tag{4}
\]
Its canonical degree-\(<N\) representative has coefficients
\[
 D_{N,j}^{\epsilon}[E_N]=\sum_{r=0}^{d}d_r\widehat B_r,\qquad
 d_r=\phi(\widehat B_rR^\epsilon L_jE_N).
 \tag{5}
\]
Indeed (1) extracts the coefficient \(d-r\) before applying \(T\).
Formula (5) is useful because it bounds an output coefficient by the full marked pairing before reconstruction. It retains all original confluent terms and all original colors.
In particular it is not a covariance assertion for a projected coupon.

Define the rate function and its maximal value by
\[
 J(u)=\int_0^u\log(2\sin\pi t)\,dt,\quad
 g(u)=J(2u)-4J(u),\quad
 G_0=g(1/4)=2\,\mathrm{Catalan}/\pi.
\]
Here Catalan denotes \(\sum_{m=0}^{\infty}(-1)^m/(2m+1)^2\). The proved Newton estimates, with absolute powers independent of all physical colors, are
\[
 \begin{array}{ll}
 \|\widehat B_r\|_{\mathcal J}
       \le CN^5\widehat B_r(-2),&
 \log\widehat B_r(-2)=Ng(r/N)+O(\log N),\quad 0\le r\le M,\\[2mm]
 \|\widehat B_r\|_{\mathcal J}\le N^2/16,&M<r<N,
 \end{array}
 \tag{6}
\]

Both endpoints and both parities are included. These are §§2–3 of
the [full-Hermite localization theorem](actual_conway_root_star_full_jet_localization.md).

Combining (3), (5), and (6) proves the full-coefficient estimate
\[
 |d_r|\le CN^C\|E_N\|_{\mathcal J}
 \begin{cases}
   \widehat B_r(-2),&r\le M,\\
   1,&r>M.
 \end{cases}
 \tag{7}
\]
There is no sum over input coefficients and no loss depending on the
degree of the unreduced representative \(E_N\).

In particular \(E_N=1\) gives, for the whole physical leaf
\(h_j^\epsilon=T(R^\epsilon L_j)\),
\[
 |[\widehat B_r]h_j^\epsilon|
 \le
 \begin{cases}
   \exp\{Ng(r/N)+O(\log N)\},&r\le M,\\
   CN^C,&r>M.
 \end{cases}
 \tag{8}
\]
This does not assert the same bound for the separate coherent core.
The two original bands can cancel in a low coefficient. Consequently
the plateau bound on the isolated signed core is not contradicted.

## 2. Reconstructing the output and locating its angular maximum

The real number \(F\) in the next hypothesis is an exponential upper rate for the input family. It is not another polynomial. Suppose, uniformly in that specified family,
\[
 \|E_N\|_{\mathcal J}\le \exp N(F+e_N),\qquad e_N\longrightarrow0.
 \tag{9}
\]
Then
\[
 \|D_{N,j}^{\epsilon}[E_N]\|_{\mathcal J}
       \le \exp N(F+2G_0+\widetilde e_N),
       \qquad \widetilde e_N\longrightarrow0.
 \tag{10}
\]
This follows by reconstructing from (7) and using (6): the low sum is
at most a polynomial times
\(\|E_N\|_{\mathcal J}\sum_{r\le M}\widehat B_r(-2)^2\);
the high sum has only a polynomial cost. Since \(g\) has its unique
maximum \(G_0\) at \(1/4\), (10) follows uniformly. A fixed loss in
the input exponent \(F\) is preserved exactly in (10).

More strongly, (9) alone implies that the output polynomial has a
fixed angular Gaussian envelope. There are \(c,C,y_0>0\), independent
of the input family and physical character color, such that
\[
 |D_{N,j}^{\epsilon}[E_N](2\cos(\vartheta+iy))|
 \le \exp N\{F+2G_0-c(\vartheta-\pi)^2+Cy^2+\widetilde e_N\},
 \quad 0\le\vartheta\le2\pi,\ |y|\le y_0.
 \tag{11}
\]
The variables \(\vartheta\) and \(y\) describe the complex spectral ellipse \(z=2\cos(\vartheta+iy)\). Its real midpoint \(\vartheta=\pi,y=0\) is \(z=-2\). Inequality (11) gives quadratic decay away from that angle and a quadratic cost for moving a small distance off the real axis. Here and below the polynomial in (11) is the unique representative of degree less than \(N\).
There is no claim that arbitrary unreduced representatives satisfy it.

For completeness, the low Newton strip rate is
\[
 b(u,\vartheta,y)
 =\int_0^u\log|2\cos(2\pi v)-2\cos(\vartheta+iy)|\,dv-2J(u).
 \tag{12}
\]
Uniform upper Riemann sums hold on the closed range \(0\le u\le1/2\):
truncate the logarithm below, pass to uniform Riemann sums, then remove
the truncation using uniform integrability of the two circular logarithms.
This retains moving and coalescing numerator zeros. The sine factorial
error is uniformly \(O(\log N)\).

At \(y=0\), strict circular rearrangement gives
\[
 b(u,\vartheta,0)\le b(u,\pi,0)=g(u),
 \tag{13}
\]
strict for \(0<u<1/2\) and \(\vartheta\ne\pi\bmod2\pi\).
Hence \(g(u)+b(u,\vartheta,0)\) has the unique maximum \(2G_0\)
at \((u,\vartheta)=(1/4,\pi)\). Near that point, with
\(w=\vartheta-\pi+iy\), its analytic Newton action is
\[
 B(u,w)=-J\!\left(\frac12-u+\frac{w}{2\pi}\right)
        -J\!\left(\frac12-u-\frac{w}{2\pi}\right)-2J(u),
 \qquad B_{ww}(u,0)=-\frac{\tan\pi u}{2\pi}.
 \tag{14}
\]
Thus the maximum has a strict index and angular quadratic loss and a
quadratic height cost. The complementary compact set has a uniform
strict real gap, which survives small fixed complex heights. Equation
(7), not a separate core envelope, now gives the low part of (11).

For the high part (7) gives full-jet norm at most
\(\operatorname{poly}(N)\|E_N\|_{\mathcal J}\). The already proved
full Hermite interpolation estimate gives, for a canonical polynomial,
\[
 |F(2\cos(\vartheta+iy))|
       \le CN^Ce^{N|y|}\|F\|_{\mathcal J}.
 \tag{15}
\]
Choose \(y_0\) small compared with \(2G_0\) and reduce \(c\) so
\(c\pi^2< G_0\). The high part then fits beneath (11) with a
fixed loss. This proves the whole output envelope. No spectral gap
for the input \(E_N\) was required in this step.

## 3. A color away from complete causes a strict loss

A uniform norm bound alone gives Section 2. To gain a loss from the newly inserted color, the Fourier argument also needs an angular estimate for the actual input polynomial. Suppose that an actual representative of
the input, possibly an unreduced product, obeys
\[
 |E_N(2\cos(\vartheta+iy))|
 \le \exp N\{F-c_E(\vartheta-\pi)^2+C_Ey^2+e_N\},
 \quad |y|\le y_E,
 \tag{16}
\]
with \(c_E\ge0\). The empty product \(E_N=1\), \(F=0\), is allowed.
Every fixed number of angular derivatives required by the Fourier
argument follows by Cauchy's estimate on disks of radius \(1/N\) in a
smaller fixed strip. The exponent changes by \(O(1)\) there; the
polynomial-in-\(2\cos\vartheta\) reflection and periodicity handle the
endpoint disks. Thus these derivatives cost only powers of \(N\),
uniformly in the physical colors. For a fixed syntax every unreduced
representative used here has degree \(O(N)\); no arbitrary continuation
of a finite physical-color array is being differentiated.
Choose once a compact interval \(I\subset(0,1/2)\) about \(1/4\).
Uniformly for \(r/N\in I\), the exact low Newton polynomial itself
has the sharper envelope
\[
 |\widehat B_r(2\cos(\vartheta+iy))|
 \le \exp N\{g(r/N)-c_I(\vartheta-\pi)^2+C_Iy^2+e_N'\},
 \qquad c_I>0,\quad e_N'\to0.
 \tag{17}
\]
The proof is (12)–(14), now with \(u\) in a fixed compact interval:
strict rearrangement gives the angular complement gap uniformly,
and \(B_{ww}\) is uniformly negative near \(\pi\).

Therefore \(\widehat B_rE_N\) satisfies the whole-child hypothesis of
the [exact root-character Fourier theorem](actual_conway_root_character_fourier_contraction.md),
uniformly over \(r/N\in I\), with rate \(F+g(r/N)\). That exact theorem
retains the actual \(R^\epsilon\) values and normals, the missing
Fourier winding \(m=-1\), and both endpoint currents. For every fixed
\(\delta>0\), it gives some \(\gamma_\delta>0\) such that
\[
 N-j\ge\delta N,\quad r/N\in I
 \quad\Longrightarrow\quad
 |d_r|\le \exp N\{F+g(r/N)-\gamma_\delta\}.
 \tag{18}
\]
This use is not an appeal to analyticity of arbitrary physical colors.
Only the actual integer \(j\) occurs in the exact Fourier identity.

Outside \(I\), the low reconstruction cost \(2g(r/N)\) has a
fixed gap below \(2G_0\). The high reconstruction has the fixed
\(2G_0\) gap already seen in §2. Equations (6)–(7),(18) imply
\[
 \sup_{N-j\ge\delta N}
 \|D_{N,j}^{\epsilon}[E_N]\|_{\mathcal J}
 \le \exp N(F+2G_0-\eta_\delta)
 \tag{19}
\]
for all sufficiently large \(N\). Every original sign, parity,
composite level and physical input color is covered. The constants
depend on the fixed input strip bounds and \(\delta\), not on those
colors or on \(N\).

In particular (18) with \(E_N=1\) proves a uniform strict whole-leaf
coefficient loss at every macroscopic physical deficit, on each
compact regular index interval. This is stronger than only bounding
the full leaf's norm.

## 4. Iterating products and decorated turns

The first example is one physical leaf: take \(E=1\) and obtain \(T(R^\epsilon L_j)\). A second example is the product of two such leaves, followed by another decorated turn. In each case the original character remains immediately before its recorded turn. Formally, start with the empty product \(1\), form finite products, and apply
any number of operations
\[
              E\longmapsto D_j^\epsilon[E]=T(R^\epsilon L_jE).
 \tag{20}
\]
Every operation uses a distinct original physical circle color and
retained half twist. No coupon is moved through a turn. Assign the
integer count \(n(1)=0\), make it additive under products, and put
\(n(D[E])=n(E)+1\).

Every resulting coupon \(E\) with \(n(E)>0\) has:

1. the uniform full-jet upper rate \(2n(E)G_0\);
2. an angular Gaussian envelope of the form (16) at that same rate,
   with a strictly positive angular constant;
3. for each fixed \(\delta>0\), a strict full-jet loss whenever any
   one of its original physical colors satisfies \(N-j_i\ge\delta N\).

The proof is finite induction. Products use the exact norm product
rule and multiply the actual polynomial envelopes. A decorated turn
uses (10)–(11). A deficit in the newly inserted character uses (19).
A deficit in a descendant gives a strict input norm loss, which
(10) preserves. Fixed finite products and sums have only polynomial
or fixed multiplicative costs and are absorbed by reducing the positive
margin. The case \(E=1\) needed for a first leaf was explicitly included.

For any nonempty such \(E\), close the source by one further original
character:
\[
        Z_N(\mathbf j)=\phi(R^{\epsilon_0}L_{j_0}E_N).
 \tag{21}
\]
Equations (3), (16), and the same root-character theorem prove
\[
 \sup_{\mathrm{physical}\ \mathbf j}|Z_N(\mathbf j)|
       \le \exp N\{2n(E)G_0+o(1)\},
 \tag{22}
\]
and for each fixed \(\delta>0\),
\[
 \max_i(N-j_i)\ge\delta N
 \quad\Longrightarrow\quad
 |Z_N(\mathbf j)|\le \exp N\{2n(E)G_0-\gamma_\delta\}.
 \tag{23}
\]
If a descendant is far, use its norm loss and (3). If only the
closing character is far, use the exact Fourier theorem on the full
input envelope (16). In particular the root is not estimated by a
separate positive alias function.

## 5. Exact complete normalization and limitations

The [positive complete-character kernel](actual_conway_reduced_hub_source_normal_form.md)
checks the rate, not just the upper bound. For pure complete
characters the exact transform is
\[
 [\widehat B_r]D_N^0[E]
   =N\sum_{k=0}^{N-1}\widehat B_r(c_k)E(c_k).
 \tag{24}
\]
For \(r>M\) this vanishes. If all input nodal values are nonnegative,
the surviving coefficients and every output nodal value are nonnegative.
The empty input is positive, and products preserve this property.
At the smallest distinct node \(c_M\), retain just the physical grid
term \(k=M\) and \(r_N=\lfloor N/4\rfloor\):
\[
 D_N^0[E](c_M)\ge
 N\,\widehat B_{r_N}(c_M)^2E(c_M).
 \tag{25}
\]
The original sine products give
\(N^{-1}\log\widehat B_{r_N}(c_M)\to G_0\) at both parities.
At even levels the node shift from \(-2\) is \(O(N^{-2})\);
the selected quarter-index factors stay away from zero, so its
logarithmic cost is \(O(N^{-1})\). At odd levels \(c_M=-2\).
Induction through the fixed tree and the exact complete closure
\(\phi(L_NE)=N\sum_kE(c_k)\) gives
\[
 Z_N(N,\ldots,N)>0,\qquad
       \lim_N N^{-1}\log Z_N(N,\ldots,N)=2n(E)G_0.
 \tag{26}
\]
Equation (26) concerns this pure complete specialization. Thus the reference in (22)–(23) is the actual pure complete source
rate. The separate [strict-source adapter](actual_conway_reduced_hub_source_normal_form.md)
and [geometric action calculation](actual_conway_rigid_spine_and_flagged_tree_geometry.md)
identify this recursive tree with the fully flagged hub presentation.
Its rate is therefore the complete geometric action of that presentation,
not an independently chosen norm budget.

The same estimates also determine the sharp exponential cost of the
bare turn in this norm:
\[
 \lim_{N\to\infty}\frac1N
       \log\|T\|_{\mathcal J\to\mathcal J}=2G_0.
 \tag{27}
\]
For the upper bound set \(j=1,\epsilon=0\) in (7), so that
\(L_1=1\) and \(D_{N,1}^0[E]=T(E)\). Its finite reconstruction
bound is an operator estimate uniform over all inputs, and (6)
gives rate at most \(2G_0\). For the lower bound use
\(T(L_N)=h_N^0\): the input has polynomial norm, while the complete
positive source estimate gives
\(N^{-1}\log\|h_N^0\|_{\mathcal J}\to2G_0\).
Thus (27) includes all original normal directions. It does not assign
that cost to the geometric action of an arbitrary existing diagram.

The limitation of this particular induction is now explicit. It preserves a specified character multiplication immediately
before each turn. An arbitrary internal turn with no such physical
character is not charged to an existing original leaf by (20).
Adding an artificial \(L_j\), treating the turn as multiplicative,
or assigning the resulting extra \(2G_0\) to the old geometric action
would change the problem. Thus this lemma alone does not give the required geometric bound for a region without a character. The positive-probe and mixed-core propagation theorems treat that region separately; they are not consequences of pretending that (20) includes a bare turn.

The original alias identity converts (23) into a total nonempty-alias gap after a finite complementary-color expansion, with its exact scalar signs and source adapter retained. The local core packet and marked filling theorem are additional inputs. The [strict-tree assembly](actual_conway_all_strict_tree_long_twist_volume.md) combines these results with the separate estimate for regions without characters. This note proves the spectral closure lemma used there, rather than a filling theorem from the norm bound alone.
