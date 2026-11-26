# Circle traces and leaf coefficients near the complete meridian

A crossing circle contributes its ordinary quantum character, and an adjacent half-twist contributes the physical crossing operator. This note studies their trace, and the leaf coefficients obtained by a quarter-turn, while the main meridian varies near completeness. The formulas keep the crossing scalar, the ordinary-circle pivot, and the orientation-dependent quarter-turn. It proves an exact formula for pure leaves, and a relative asymptotic for half-twisted leaves on any compact interval of regular low Newton indices. In particular the moving leaf ratio is derived from its finite source, rather than inferred from the bounded turn multiplier. The [Newton compiler](actual_main_meridian_newton_compiler.md) fixes the orientation spaces and cut pairing; the [turn comparison](actual_main_meridian_turn_comparison.md) fixes the coordinate formula used below. Section 10 constructs the canonical Gamma interpolation needed in the [grouped wire packet](actual_main_meridian_grouped_wire_packet.md). The [direct crossing trace](actual_main_meridian_direct_crossing_trace.md) then treats arbitrary fixed crossing powers. A relative profile for a whole knot requires the additional global comparisons in the [filled-volume theorem](actual_main_meridian_filled_volume.md).

## 1. Coordinates and the exact coefficient extractor

Put
\[
q=e^{\pi i/N},\quad d=N-1,\quad Q=q^2,\quad M=q^s,
\qquad c_a=2\cos((2a+1)\pi/N),
\]
\[
S_n=\prod_{a=1}^n2\sin(\pi a/N),\qquad
 e_r(z)=S_r^{-2}\prod_{a=0}^{r-1}(c_a-z),\qquad 0\le r<N.
\tag{1}
\]
These are the fixed complete Newton polynomials. The input algebra is the equal-color algebra
\[
P_s(z)=\mathcal T_N(z)+2\cos2\pi s,
\qquad
\phi_s(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_s}F.
\tag{2}
\]
Here \(\mathcal T_N(u+u^{-1})=u^N+u^{-N}\). The actual circle polynomial and equal-color checked crossing are
\[
L_j(z)=(-1)^{j-1}U_{j-1}(z/2),\qquad
\kappa_s=q^{(d+s)^2/2},\qquad
\lambda_a=(-1)^a q^{a(a+1)}q^{-2sa}.
\tag{3}
\]
The full crossing has values \(\kappa_s\lambda_a\) at the moving roots, with its holomorphic repeated-root continuation. Its inverse is interpreted in the same physical quotient.

Write the typed fixed-coordinate turn as
\[
T_s=\frac{\gamma_N(s)}{H_N(s)}\mathcal R\operatorname{diag}(W_n(s)),
\qquad \mathcal R e_n=e_{d-n},
\tag{4}
\]
\[
H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad
W_n(s)=\prod_{a=1}^n
 \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi a/N)}\right).
\tag{5}
\]
The scalar \(\gamma_N(s)\) is the prescribed one among \(1,q^{s^2/2},q^{-s^2/2}\). In particular the turn from equal-color \(++\) endomorphisms to the mixed morphism space has \(\gamma_N(s)=q^{-s^2/2}\). All values at zero are removable. The exact identity
\(W_rW_{d-r}=H_N^2\) gives the physical coefficient
\[
h_{N,s}^{\epsilon}(r,j)
 :=[e_r]T_s(R_s^\epsilon L_j)
 =\gamma_N(s)\frac{H_N(s)}{W_r(s)}
       \phi_s(e_rR_s^\epsilon L_j),\qquad \epsilon\in\{0,1,-1\}.
\tag{6}
\]
Every scalar in (6) is retained. The formula is in a specified input/output frame, not an identification of all orientation types without their carriers.

## 2. Pure leaves: an exact identity at every auxiliary color

For every physical \(1\le j\le N\) and every \(0\le r<N\),
\[
\boxed{h_{N,s}^{0}(r,j)
 =\gamma_N(s)\frac{H_N(s)}{W_r(s)}h_{N,0}^{0}(r,j).}
\tag{7}
\]
Indeed \(\deg(e_rL_j)\le2N-2\). If this polynomial is divided by \(P_0\), its quotient has degree at most \(N-2\). Replacing \(P_0\) by \(P_s=P_0+\Delta_s\) changes the remainder by \(-\Delta_s\) times that quotient, of degree at most \(N-2\). Its top coefficient is unchanged. Thus \(\phi_s(e_rL_j)=\phi_0(e_rL_j)\), proving (7). This includes zeros of the complete coefficient; it is an identity of coefficients rather than a ratio asserted at those zeros.

For the complete ordinary color \(j=N\), the low coefficient is exactly
\[
h_{N,0}^{0}(r,N)=N^2\frac{S_{2r}}{S_r^4},\qquad 2r<N.
\tag{8}
\]
The pure result therefore already includes every physical deficit, both parities, and every pre-resonance compact main disk \(|s|\le R<1\).

## 3. Complete auxiliary color: exact shifted-grid formula

Let
\[
\tau_a(s)=\frac{2\pi}{N}\left(\frac d2+s-a\right),\qquad
C_{N,\epsilon}(s)=q^{\epsilon(d^2/4-s^2/2)}.
\tag{9}
\]
The full crossing values, including the Cartan scalar, obey
\[
 (\kappa_s\lambda_a)^\epsilon
 =C_{N,\epsilon}(s)
     \exp\left(\frac{i\epsilon N\tau_a(s)^2}{4\pi}\right).
\tag{10}
\]
Since \(L_N=(-1)^dP_s'/N\), ordinary Lagrange interpolation first at generic \(s\), followed by holomorphic continuation, proves
\[
\phi_s(e_rR_s^\epsilon L_N)
 =N C_{N,\epsilon}(s)\,\mathcal Q_{N,r}^\epsilon(s),
\tag{11}
\]
\[
\mathcal Q_{N,r}^\epsilon(s)
 =\sum_{a=0}^{N-1}
 e_r(-2\cos\tau_a(s))
 \exp\left(\frac{i\epsilon N\tau_a(s)^2}{4\pi}\right).
\tag{12}
\]
Formula (11) retains the full confluent trace at \(s=0\), including the simple last node at odd levels. It is not a replacement of a repeated-root trace by arbitrary nodal values: the factor \(P_s'\) makes this particular root sum exact.

Fix a compact \(I\subset(0,1/2)\), and write \(x=r/N\in I\). For \(|\tau|\) small, the numerator of \(e_r(-2\cos\tau)\) is nonzero. Direct differentiation gives
\[
\frac{d^2}{d\tau^2}\log e_r(-2\cos\tau)\bigg|_{\tau=0}
 =-\frac12\sum_{a=0}^{r-1}\sec^2\left(\frac{\pi(a+1/2)}N\right)
 =-\frac{N}{2\pi}\tan\pi x+O(N^{-1}).
\tag{13}
\]
All fixed higher derivatives are \(O_I(N)\) on a fixed smaller disk. The complete Newton angular estimate also gives constants \(c,C,y_0>0\), uniformly in \(x\in I\), such that
\[
|e_r(-2\cos(t+iy))|
 \le \operatorname{poly}(N)e^{Ng(x)}
       e^{-Nc t^2+NCy^2},\qquad |t|\le\pi,\quad |y|\le y_0.
\tag{14}
\]
Here \(g(x)=J(2x)-4J(x)\), with \(J(x)=\int_0^x\log(2\sin\pi u)\,du\). The factor at zero satisfies
\[
e_r(-2)=\frac{e^{Ng(x)}}{2N\sin\pi x}\,[1+O_I(N^{-1})].
\tag{15}
\]
The numerator uses midpoint Euler--Maclaurin; the denominator uses the usual sine-factorial expansion. Both expansions are uniform on \(I\).

## 4. Exponentially accurate grid shift and a nonzero anchor

For every \(R_0<1/2\), there is \(c_0>0\) such that
\[
\mathcal Q_{N,r}^\epsilon(s)
 =\frac{N}{2\pi}\int_{-\pi}^{\pi}
       e_r(-2\cos t)e^{i\epsilon Nt^2/(4\pi)}\,dt
   +O\left(e^{N(g(x)-c_0)}\right),\quad |s|\le R_0,
\tag{16}
\]
where polynomial factors have been absorbed by decreasing \(c_0\). The same statement holds for \(\epsilon=0\).

Here is the quadrature proof, including the nonperiodic endpoints of the chirp. Set \(\eta=(-1)^{N+1}\), \(a_s=\eta e^{2\pi is}\), and
\[
K_s(\tau)=\frac{iNe^{iN\tau}}{e^{iN\tau}-a_s}.
\tag{17}
\]
On a rectangle with vertical sides \(\operatorname{Re}\tau=\pm\pi\) and horizontal sides \(\operatorname{Im}\tau=\pm y\), its residues select exactly the \(N\) points in (12). On the upper horizontal side \(K_s=O_R(Ne^{-Ny})\); on the lower side \(K_s=iN+O_R(Ne^{-Ny})\). On the vertical sides \(|K_s|\le C_RN\), by the same positive-ray denominator estimate used for the paired-grid contour. The integrand apart from \(K_s\) is bounded by
\(\operatorname{poly}(N)\exp N(g-ct^2+Cy^2+|ty|/(2\pi))\).
Choose fixed \(y>0\) small. Completing the square makes the horizontal error at most \(\exp N(g-y+C'y^2)\). The vertical sides have a fixed strict deficit. Move the lower straight integral to the real segment; its two connecting vertical integrals have the same deficit. This proves (16) without making the chirp periodic or discarding an endpoint current.

The integral in (16) is nonzero for large \(N\). Its elementary local Gaussian expansion, using (13), is
\[
\frac{N}{2\pi}\int_{-\pi}^{\pi}
 e_r(-2\cos t)e^{i\epsilon Nt^2/(4\pi)}\,dt
 =\frac{\sqrt N\,e_r(-2)}{\sqrt{\tan\pi x-i\epsilon}}
       [1+O_I(N^{-1})].
\tag{18}
\]
The square root has positive real part. The complement of a fixed small neighborhood is exponentially smaller by (14). On that neighborhood, the analytic fourth-order remainder and Gaussian integration give the uniform \(O(N^{-1})\) relative error. Thus (16) has a lower bound of a fixed multiple of \(\sqrt N e_r(-2)\). In particular,
\[
\frac{\mathcal Q_{N,r}^\epsilon(s)}{
      \mathcal Q_{N,r}^\epsilon(0)}
 =1+O(e^{-c_0'N}),\qquad |s|\le R_0.
\tag{19}
\]

## 5. The actual complete-color leaf ratio and first correction

Combining (6), (11), and (19) gives
\[
\boxed{\displaystyle
\frac{h_{N,s}^{\epsilon}(r,N)}{h_{N,0}^{\epsilon}(r,N)}
 =\gamma_N(s)\frac{H_N(s)}{W_r(s)}q^{-\epsilon s^2/2}
       [1+O_{I,R}(e^{-cN})],}
\tag{20}
\]
for every compact \(I\subset(0,1/2)\), every fixed \(R<1\), both parities, and \(\epsilon=0,\pm1\). For \(\epsilon=0\), (20)'s error is exactly zero.

To justify the full radius \(R<1\), first use (19) on any fixed smaller disk \(R_0<1/2\). Divide the actual coefficient by the explicit nonvanishing prefactor and its nonzero complete coefficient. The resulting error is holomorphic on \(|s|<1\). On every larger fixed disk \(R'<1\), the physical leaf coefficient cone in the [source-bound theorem](actual_main_meridian_source_bounds.md), Section 1 bounds its magnitude by a power of \(N\): its numerator is \(\operatorname{poly}(N)e^{Ng(x)}\), while (15),(18) bound its complete denominator below by \(\operatorname{poly}(N)^{-1}e^{Ng(x)}\). Hadamard's three-circles inequality between \(R_0\) and \(R'\) keeps a strictly negative exponential exponent on every intermediate radius. This extends (20). This step uses actual holomorphy through the removable collision at \(s=\pm1/2\), not the chosen unwrapped grid as a formula outside its original rectangle.

The paired bulk product has the uniform expansion
\[
\log\frac{W_r(s)}{H_N(s)}
 =\frac{\pi s^2}{N}\cot\pi x+O_{I,R}(N^{-2}).
\tag{21}
\]
For completeness, compare \(r\) to the midpoint. At odd \(N\), \(H_N=W_{(N-1)/2}\); at even \(N\), \(H_N=W_{N/2-1}\cos(\pi s/N)\). Expand only the intervening factors, whose indices lie in a compact interior interval. Their logarithmic sum is
\(-\pi^2s^2N^{-2}\sum\csc^2(\pi a/N)+O(N^{-3})\), and the elementary integral of \(\csc^2\) gives (21). The even extra cosine changes only the \(O(N^{-2})\) term.

Write \(\gamma_N(s)=q^{\alpha s^2/2}\), with \(\alpha\in\{-1,0,1\}\) fixed by the actual orientation. Then
\[
\boxed{\displaystyle
\frac{h_{N,s}^{\epsilon}(r,N)}{h_{N,0}^{\epsilon}(r,N)}
 =1+\frac{s^2}{N}
    \left[-\pi\cot\pi x+\frac{i\pi}{2}(\alpha-\epsilon)\right]
    +O_{I,R}(N^{-2}).}
\tag{22}
\]
Every fixed \(s\)-derivative has the corresponding error on smaller disks by Cauchy's estimate. This identifies the leading amplitude and its first main-meridian correction. The physical chirp scalar and the typed-turn scalar both contribute, even though the leading ratio tends to one.

For the \(++\) input, \(\alpha=-1\). For an opposite-color input expressed in the prescribed mixed reference, the quotient is constant and the crossing polynomial is the fixed complete \(r_0\), up to its explicitly retained scalar monodromy factors. In that case the trace itself is independent of \(s\); its ratio is exactly \(\gamma_N(s)H_N/W_r\) times those scalar factors. The extra factor \(q^{-\epsilon s^2/2}\) in (20) belongs to the moving equal-color crossing, not to a constant opposite-color crossing. Frame factors must be applied according to the actual six-type table.

## 6. A joint continuation for small auxiliary deficits

This section gives a concrete holomorphic continuation of the actual physical grid near \(j=N\). It does not assert that every possible off-integer continuation is equal to it. Put \(h=Nt\), with \(t\) complex and small, and retain the unwrapped grid from (9). Let
\[
F_{N,r}^{\epsilon}(\tau)=e_r(-2\cos\tau)e^{i\epsilon N\tau^2/(4\pi)},
\]
\[
A_{N,r}^\epsilon(s,t)=\sum_aF_{N,r}^{\epsilon}(\tau_a(s))\cos(Nt\tau_a(s)),
\quad
B_{N,r}^\epsilon(s,t)=\sum_aF_{N,r}^{\epsilon}(\tau_a(s))\sin(Nt\tau_a(s)).
\tag{23}
\]
Define
\[
\widetilde h_{N,s}^{\epsilon}(r,t)
 =\gamma_N(s)\frac{H_N(s)}{W_r(s)}
       N C_{N,\epsilon}(s)
       \left[A_{N,r}^\epsilon(s,t)-\cot(2\pi s)B_{N,r}^\epsilon(s,t)\right].
\tag{24}
\]
The value at \(s=0\) is removable: the grid is symmetric there, the first factor is even in \(\tau\), and \(B(0,t)=0\). Formula (24) is holomorphic jointly for \(|s|<1/2\) and all finite \(t\). At every physical integer \(h\), \(j=N-h\) in its original range, it is exactly the physical coefficient. This follows directly from the generic-root trace and
\[
\sin((N-h)\tau_a(s))
 =\eta\left[\sin2\pi s\cos(h\tau_a(s))
             -\cos2\pi s\sin(h\tau_a(s))\right].
\tag{25}
\]
Its complete value therefore keeps the true repeated-root normal contribution, including the derivative implicit in \(\cot(2\pi s)B(s,t)\).

For each \(R<1/2\) and compact \(I\), choose a sufficiently small fixed \(t_0>0\). The same rectangle proof gives, uniformly on \(|s|\le R\), \(|t|\le t_0\),
\[
A_{N,r}^\epsilon(s,t)=\frac N{2\pi}\int_{-\pi}^{\pi}
 F_{N,r}^{\epsilon}(\tau)\cos(Nt\tau)\,d\tau
 +O(e^{N(g(x)-c)}),\qquad B_{N,r}^\epsilon(s,t)=O(e^{N(g(x)-c)}).
\tag{26}
\]
The integral of the sine term vanishes by oddness. On a slightly larger \(s\)-disk, the same bound and \(B(0,t)=0\) bound the product \(\cot(2\pi s)B(s,t)\) holomorphically through zero. The additional exponential cost \(e^{N\pi|\operatorname{Im}t|+N|t|y}\) is absorbed by taking \(t_0\) small before fixing the gap.

The integral in (26) has a unique analytic saddle near zero and a nonzero leading amplitude. Define the analytic logarithmic action near \(\tau=0\)
\[
b(x,\tau)=\int_0^x\log(2\cos2\pi v+2\cos\tau)\,dv-2J(x),
\]
\[
\Psi_\epsilon(x,\tau,t)=b(x,\tau)+\frac{i\epsilon\tau^2}{4\pi}+it\tau,
\qquad \partial_\tau\Psi_\epsilon(x,\tau_*,t)=0,\quad \tau_*(x,0)=0.
\tag{27}
\]
Its Hessian at zero is \(-(\tan\pi x-i\epsilon)/(2\pi)\), bounded away from zero. A small analytic contour displacement through \(\tau_*\), retaining exponentially small vertical endpoints, proves a uniform relative \(1+O(N^{-1})\) saddle expansion. In particular its modulus is at least \(\operatorname{poly}(N)^{-1}\exp N(g(x)-C|t|^2)\) after shrinking \(t_0\). Thus
\[
\boxed{\displaystyle
\frac{\widetilde h_{N,s}^{\epsilon}(r,t)}{
      \widetilde h_{N,0}^{\epsilon}(r,t)}
 =\gamma_N(s)\frac{H_N(s)}{W_r(s)}q^{-\epsilon s^2/2}
       [1+O(e^{-c'N})],\quad |s|\le R<1/2,\quad |t|\le t_0.}
\tag{28}
\]
The first correction (22) consequently holds for this joint continuation as well, uniformly in its small complex \(t\)-disk. At physical integer deficits this is a statement about the actual leaf. No analytic continuation through the additional resonances of (24) at \(s=\pm1/2\) is claimed for noninteger \(h\).

For physical integer deficits alone, (28) extends to every fixed \(R<1\) after possibly shrinking \(t_0\) depending on \(R\). On a larger disk \(R'<1\), the actual coefficient cone and the complete saddle lower bound give a normalized bound \(\operatorname{poly}(N)e^{Ct_0^2N}\). On a fixed disk below \(1/2\), the error in (28) is \(O(e^{-cN})\). The three-circles inequality bounds its logarithmic rate on the intermediate disk by
\[
-\beta c+(1-\beta)Ct_0^2,
\qquad
\beta=\frac{\log(R'/R)}{\log(R'/R_0)}>0.
\tag{28a}
\]
Choose \(t_0\) so that this is negative. The constants are uniform over all physical \(0\le h/N\le t_0\) and all wire indices in \(I\). This extension uses the actual physical polynomial at each integer color; it does not assert that the off-integer function (24) is regular through \(s=\pm1/2\).

## 7. The auxiliary action and leading amplitude are the old selected ones

The saddle of (27) also identifies the continuation's complete asymptotic. Midpoint Euler--Maclaurin gives, uniformly on a small complex \(\tau\)-neighborhood,
\[
e_r(-2\cos\tau)=\frac{1}{2N\sin\pi x}
                 e^{Nb(x,\tau)}[1+O(N^{-1})].
\tag{29}
\]
After removing exactly the old unit phase \(e^{i\epsilon\pi d/4}\), (24) at \(s=0\) has leading action and amplitude
\[
f_\epsilon(x,t)=\Psi_\epsilon(x,\tau_*(x,t),t),\qquad
\beta_\epsilon(x,t)=
 \frac{e^{-i\epsilon\pi/4}}
 {2\sin\pi x\sqrt{2\pi[-\partial_\tau^2\Psi_\epsilon(x,\tau_*,t)]}},
\tag{30}
\]
\[
e^{-i\epsilon\pi d/4}\widetilde h_{N,0}^{\epsilon}(r,t)
 =N^{1/2}\beta_\epsilon(x,t)e^{Nf_\epsilon(x,t)}[1+O(N^{-1})].
\tag{31}
\]
The square root continues the positive-real branch when \(\epsilon=t=0\). At completeness,
\[
f_\epsilon(x,0)=g(x),\quad
\beta_0(x,0)=\frac{1}{2\sin\pi x\sqrt{\tan\pi x}},\quad
\frac{\beta_\epsilon(x,0)}{\beta_0(x,0)}
 =\sqrt{\sin\pi x}\,e^{-i\epsilon\pi x/2}\quad(\epsilon=\pm1).
\tag{32}
\]
These agree with the actual complete phase and amplitude; no parity phase has been changed.

The pure saddle action is
\[
g(x,t)=J(2x)-2J(x)-J(x-t)-J(x+t).
\tag{33}
\]
One direct verification uses
\[
b_\tau(x,\tau)=-\frac1\pi\operatorname{artanh}
       \left(\tan\pi x\tan\frac\tau2\right).
\tag{34}
\]
At the pure saddle, \(\tan(\tau_*/2)=i\tan(\pi t)/\tan(\pi x)\), and hence \(i\tau_*=\partial_tg(x,t)\). The actions agree at \(t=0\), proving (33). With a half-twist, introduce \(u\) by
\[
t=u-\frac{\epsilon}{2\pi i}g_u(x,u).
\]
Then substitution into (27) gives exactly
\[
f_\epsilon(x,t)=g(x,u)-\frac{\epsilon}{4\pi i}g_u(x,u)^2.
\tag{35}
\]
This is the shear selected in the [complex-color source packet](actual_odd_conway_complex_color_packet.md). Equations (30)--(35) provide its nonzero leading amplitude on every compact regular low-index interval. They do not by themselves identify all subleading terms of every alternative off-integer factorial interpolation; (24) is the explicitly chosen continuation in the moving parameter.

## 8. Scope of the coefficient statements

The exact pure identity holds for every physical auxiliary color. The half-twisted complete-color theorem (20)--(22) holds for every compact regular low-index interval and every main disk \(R<1\). The joint small-deficit continuation (24)--(35) is proved on \(R<1/2\); it agrees exactly with every physical color on its grid and has an exponential relative grid-shift error. The statements are all-level, with the original parity, crossing and typed-turn factors intact.

The proof does not control the entire coefficient range or supply a deformed global source lower bound. It also does not compare a filled invariant to its own smaller volume. The estimates through Section 9 are uniform over the physical integer low-index window. Section 10 supplies a specified analytic factorial-and-integral continuation in the complex wire coordinate, with exponential agreement on that physical grid.

## 9. A whole circle-carrying junction

The same argument applies to a fixed number \(B\ge1\) of low Newton factors. Define
\[
E_{N,\mathbf n}(z)=\prod_{a=1}^B e_{n_a}(z),\qquad
V_{N,s}^{\epsilon}(\mathbf n)
 =\phi_s\left(R_s^\epsilon L_NE_{N,\mathbf n}\right),
\qquad 0\le n_a\le\lfloor(N-1)/2\rfloor.
\tag{36}
\]
The raw product is retained inside the trace; its degree need not be less than \(N\). Lagrange interpolation still gives exactly
\[
V_{N,s}^{\epsilon}(\mathbf n)
 =N C_{N,\epsilon}(s)
   \sum_{r=0}^{N-1}E_{N,\mathbf n}(-2\cos\tau_r(s))
       e^{i\epsilon N\tau_r(s)^2/(4\pi)}.
\tag{37}
\]
No quotient norm or termwise estimate of the new multiplication sectors enters this identity.

There is an all-index bound by the complete positive tensor:
\[
\boxed{|V_{N,s}^{\epsilon}(\mathbf n)|
       \le C_{B,R}N\,V_{N,0}^{0}(\mathbf n),\qquad |s|\le R<1.}
\tag{38}
\]
Here every low index, including zero and the endpoint, is allowed. To prove it, use the positive Laurent coefficients
\[
e_n(-u-u^{-1})
 =\sum_{k=-n}^{n}
   \frac{S_{2n}}{S_n^2S_{n-k}S_{n+k}}u^k,
 \qquad 2n<N.
\tag{39}
\]
At the shifted grid, \(|\operatorname{Im}\tau_r(s)|\le2\pi R/N\). Therefore
\[
|e_n(-2\cos\tau_r(s))|
 \le e^{2\pi Rn/N}e_n(-2)\le e^{\pi R}e_n(-2).
\tag{40}
\]
The chirp and its full scalar in (37) are bounded there by a constant depending only on \(R\). Thus the left side of (38) is at most \(C_{B,R}N^2\prod_a e_{n_a}(-2)\).

At completeness every low factor is nonnegative at every Casimir node: it vanishes at a previous node, and otherwise all its defining factors have the same positive ordering. Consequently
\[
V_{N,0}^0=N\sum_{r=0}^{N-1}E_{N,\mathbf n}(-2\cos\tau_r(0)).
\tag{41}
\]
At odd levels a node is exactly \(-2\), giving \(V_{N,0}^0\ge N\prod e_{n_a}(-2)\). At even levels put \(N=2m\), \(\theta=\pi/N\). The closest node is \(-2\cos\theta\), and
\[
\frac{e_n(-2\cos\theta)}{e_n(-2)}
 =\prod_{a=0}^{n-1}
   \frac{\cos(a\theta)\cos((a+1)\theta)}
        {\cos^2((a+1/2)\theta)}.
\tag{42}
\]
Each factor is positive and at most one, by the concavity of \(\log\cos\) on this interval. Hence (42) decreases with \(n\). The ordinary cosine products at the maximal allowed \(n=m-1\) give
\[
\prod_{a=1}^{m-1}\cos(a\theta)=\frac{\sqrt m}{2^{m-1}},\qquad
\prod_{a=0}^{m-1}\cos((a+1/2)\theta)=2^{1/2-m},
\]
\[
\frac{e_{m-1}(-2\cos\theta)}{e_{m-1}(-2)}
 =m\tan(\theta/2)\ge\frac\pi4.
\tag{43}
\]
This includes \(m=1\) with the empty-product interpretation. Thus
\[
V_{N,0}^0(\mathbf n)
 \ge N(\pi/4)^B\prod_a e_{n_a}(-2)
\tag{44}
\]
at every parity, proving (38). The comparison is with the actual complete pure tensor at the same level; no adjacent-level substitution or unproved signed lower bound is used.

Now assume all \(x_a=n_a/N\) lie in a fixed compact \(I\subset(0,1/2)\). The product satisfies (14) with summed curvature
\[
T(\mathbf x)=\sum_{a=1}^B\tan\pi x_a>0.
\tag{45}
\]
The rectangle quadrature and nonzero Gaussian anchor become
\[
\sum_r E_{N,\mathbf n}(-2\cos\tau_r(0))
 e^{i\epsilon N\tau_r(0)^2/(4\pi)}
 =\frac{\sqrt N\prod_a e_{n_a}(-2)}
        {\sqrt{T(\mathbf x)-i\epsilon}}[1+O(N^{-1})].
\tag{46}
\]
Every constant is uniform on the fixed product window. Equations (37), (46), and the same three-circles argument prove
\[
\boxed{\displaystyle
\frac{V_{N,s}^{\epsilon}(\mathbf n)}{V_{N,0}^{\epsilon}(\mathbf n)}
 =q^{-\epsilon s^2/2}[1+O_{B,I,R}(e^{-cN})],
 \qquad |s|\le R<1.}
\tag{47}
\]
For the extension step, (38) and (46) bound the normalized holomorphic family polynomially on every larger compact main disk, since the complete pure and half-twisted Gaussian anchors have the same nonzero rate. No moving high-degree canonical polynomial stability is assumed. The first correction is therefore \(-i\epsilon\pi s^2/(2N)+O(N^{-2})\), before any typed-turn scalar belonging to an adjacent edge is applied.

Multilinear expansion of (38) also bounds arbitrary complex low arrays by the complete pure tensor of their absolute coefficient arrays. Equation (47), in contrast, is a local kernel statement on the regular product window. For signed sums it gives an error bounded by the absolute complete-window majorant; a relative statement for the sum still requires a noncancellation comparison.

Finally, replacing \(e_r\) by \(E_{N,\mathbf n}\) in (23)--(28) gives the same small-deficit continuation for a whole circle-carrying junction. Its saddle uses \(\sum_a b(x_a,\tau)+i\epsilon\tau^2/(4\pi)+it\tau\), with Hessian \(-(T(\mathbf x)-i\epsilon)/(2\pi)\). The relative factor is again \(q^{-\epsilon s^2/2}\) with exponential error on \(R<1/2\) and a sufficiently small complex \(t\)-disk. The original integer auxiliary colors, pivot, and full crossing are retained. This local extension does not by itself establish the filled source's absolute-window/noncancellation comparison.

## 10. An explicit joint analytic interpolation in the wire variable

The grid-only qualification in Section 8 can be removed locally by constructing, rather than postulating, an analytic interpolant. This does not change any finite coefficient. Use the existing canonical sine-factorial function
\[
G_N(z)=\left(\frac{2\pi}{N}\right)^z\Gamma(z+1)
 \prod_{k\ge1}\frac{\Gamma(Nk+z+1)}
 {\Gamma(Nk-z)(Nk)^{2z+1}},\qquad -1<\operatorname{Re}z<N,
\tag{48}
\]
with its fixed positive-base logarithms. It is holomorphic and nonzero on this strip, obeys \(G_N(0)=1\), \(G_N(r)=S_r\), and
\(G_N(z+1)/G_N(z)=2\sin(\pi(z+1)/N)\). The [exact factorial interpolation theorem](exact_factorial_interpolation_and_complex_contours.md) proves these facts and the uniform complex bulk expansion. The normalization in (48) is fixed; it cannot be changed by multiplying by an unspecified periodic function.

For complex \(x\) near \(I\) and small complex \(\tau\), define \(u=N\tau/(2\pi)\) and
\[
\mathcal E_N(x,\tau)=
 \frac{G_N(d/2+u)G_N(d/2-u)}
 {G_N(d/2-Nx+u)G_N(d/2-Nx-u)G_N(Nx)^2}.
\tag{49}
\]
At every physical \(x=r/N\), the exact shift identity shows
\(\mathcal E_N(r/N,\tau)=e_r(-2\cos\tau)\). Indeed the two numerator-to-denominator ratios are the products of \(2\cos((a+1/2)\pi/N\mp\tau/2)\), whose product is the defining Newton numerator. All arguments in (49) stay in fixed complex bulk strips after choosing the \(x\)-neighborhood and the \(\tau\)-disk sufficiently small. Hence (49) is analytic there, with the uniform expansion (29).

Likewise set
\[
\mathcal W_N(x,s)=
 \frac{G_N(Nx-s)G_N(Nx+s)}
 {G_N(Nx)^2G_N(-s)G_N(s)}.
\tag{50}
\]
At physical \(x=r/N\) this is exactly \(W_r(s)\). The two endpoint factors in (50) are nonzero on \(|s|<1\), and the other factors are in the same regular bulk domain.

The canonical product makes the endpoint cancellation explicit. Gamma reflection and the paired factors in (48) give
\[
G_N(s)G_N(-s)
 =\frac{\pi s}{\sin\pi s}
     \prod_{k\ge1}\left(1-\frac{s^2}{N^2k^2}\right)
 =\frac{N\sin(\pi s/N)}{\sin\pi s}
 =\frac1{H_N(s)}.
\tag{50a}
\]
Consequently
\[
\frac{H_N(s)}{\mathcal W_N(x,s)}
 =\frac{G_N(Nx)^2}{G_N(Nx-s)G_N(Nx+s)}.
\tag{50b}
\]
Thus the exact turn factor in the local interpolation is a ratio of three regular bulk factorials; it has no unknown endpoint normalization.

Choose a fixed small real \(a>0\) inside that domain, and define the concrete interpolant
\[
\mathfrak h_N^\epsilon(x,s,t)=
 \gamma_N(s)\frac{H_N(s)}{\mathcal W_N(x,s)}
 \frac{N^2 C_{N,\epsilon}(s)}{2\pi}
 \int_{-a}^{a}\mathcal E_N(x,\tau)
     e^{i\epsilon N\tau^2/(4\pi)}\cos(Nt\tau)\,d\tau.
\tag{51}
\]
It is jointly holomorphic on fixed smaller neighborhoods in \(x,t,s\). Its saddle remains strictly inside the integration endpoints after shrinking these neighborhoods. The endpoint contributions are exponentially smaller uniformly, and the saddle amplitude is nonzero. Equations (16),(26) and the real-grid Newton tail estimate show
\[
\widetilde h_{N,s}^{\epsilon}(r,t)
 =\mathfrak h_N^\epsilon(r/N,s,t)
          [1+O(e^{-cN})]
\tag{52}
\]
uniformly over the physical regular wire indices, \(|s|\le R<1/2\), and a sufficiently small fixed complex \(t\)-disk. For integer \(Nt\) in the physical range, the left side is the literal physical coefficient. The same construction at \(t=0\), combined with Section 5, works on every fixed main disk \(R<1\). More generally, (28a) proves that (51) is an exponentially accurate analytic interpolation of all the physical integer-deficit rows on any fixed \(R<1\), with the small \(t\)-neighborhood chosen depending on that radius. The interpolant itself is holomorphic for complex \(t\) throughout that neighborhood. Its comparison beyond \(R=1/2\) is asserted on the physical integer rows, not as equality with the resonant unwrapped continuation (24).

The interpolation itself has the exact ratio
\[
\frac{\mathfrak h_N^\epsilon(x,s,t)}{
      \mathfrak h_N^\epsilon(x,0,t)}
 =\gamma_N(s)\frac{H_N(s)}{\mathcal W_N(x,s)}q^{-\epsilon s^2/2}.
\tag{53}
\]
There is no unknown meridian-dependent amplitude in (53). Its first correction is (22), now holomorphically in \(x\) on a smaller neighborhood, by the same bulk factorial expansion. The full leading action and amplitude are (30),(31). The construction is valid on either side of \(x=1/4\), since its Gaussian Hessian is nonzero throughout the entire compact interval \(I\subset(0,1/2)\).

For a circle-carrying junction, replace \(\mathcal E_N(x,\tau)\) in (51) by \(\prod_{a=1}^B\mathcal E_N(x_a,\tau)\), and omit the turn factor if the quantity is the junction trace itself. This gives the corresponding joint analytic interpolation of (37) and its small-deficit version. Its exact main ratio is \(q^{-\epsilon s^2/2}\); edge turn factors remain separate. The comparison to the physical grid is exponentially accurate with the same proof.

These interpolants supply the local analytic input needed for a complex wire saddle. They do not supply a global bound for a signed contraction, its off-window states, or a filled invariant. The [component extension](actual_main_meridian_component_extension.md) supplies the grouped high-index comparison, and the [grouped wire packet](actual_main_meridian_grouped_wire_packet.md) supplies the finite-window and contour arguments. Those are separate inputs from the local meridian dependence identified here.
