# Output uniformity of the critical fold remainder

Private written proof, 16 November 2026.

The optimized physical-block fold estimate extends to a fixed real
output interval and a complex spectral tube of width \(N^{-1}\)
around it. At the angular branch point this includes a complex
angular disk of radius \(O(N^{-1/2})\). Fixed ordinary output
derivatives cost \(N^q\). The critical estimate comes from the
literal shortened Newton kernel, not continuation of a scalar
estimate at complete output.

This does not supply the fixed complex output neighborhood required
by the upper-packet composition theorem. Its fold comparison has
the opposite sign on a fixed imaginary output angle. That is a
limitation of this estimate, not a lower bound for the whole source.

## 1. The same actual remainder, with free output

Use the source, rowwise optimized integer cutoffs, actual common
fold anchor, and mirrored block rectangles of the pinned optimized
assembly. Fix \(r\ge1\), real microscopic parameters
\(|\alpha_i|\le A_{\rm in}\), and \(n=2\sigma\), \(\sigma=\pm1\).
Put \(h=N^{-1}\), and
\[
 B_N(C)=\prod_{i=1}^r K_N(2\cosh(\alpha_i h),C),\qquad
 Z(u)=-2\cos u .
 \tag{1}
\]
Replace the outgoing complete-color kernel by its actual free
output polynomial throughout:
\[
 L_N(t,Z)=\sum_{k<\lfloor N/2\rfloor}e_k(-2\cos t)e_k(Z).
 \tag{2}
\]
Here \(e_k(C)=S_k^{-2}\prod_{a<k}(c_a-C)\),
\(c_a=2\cos((2a+1)\pi/N)\), and
\(S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N)\).
Let \(\mathcal V_{\rm out,N}(Z)\) be precisely the four outer
baseline half-sides of that assembly, with (2) in their integrands.
The cutoffs and incoming baseline anchors do not depend on \(Z\).
Define the actual holomorphic remainder
\[
 \mathcal E_N(Z)=
 \phi_{\mathcal C_N}[R_N^n B_N K_N(\cdot,Z)]
                              -\mathcal V_{\rm out,N}(Z).
 \tag{3}
\]
The original high sector and every physical first normal remain
in (3). The exterior sides are not deleted.

Write \(W_\sigma(u)\) for the original two-power stationary action
from the local wire theorem, with its specified additive constant
and signed saddle. It is even and holomorphic near \(u=0\), so it
defines a holomorphic function \(\mathcal W_\sigma(Z)\) near
\(Z=-2\). Its real complete value is \(\mathcal I_2=2G/\pi\).

Choose a sufficiently small fixed \(u_0>0\), and set
\[
 \mathcal I_{\rm out}=[-2,-2\cos u_0],\qquad
 \mathcal T_{A,N}=\{Z:\operatorname{dist}(Z,\mathcal I_{\rm out})
                                                   \le A/N\}.
 \tag{4}
\]
For \(Z\) in this tube, let \(Z_s\) be its nearest point on this
real segment and write \(Z_s=-2\cos u_s\), \(0\le u_s\le u_0\).
This is only a reference for estimates, not a holomorphic map.

**Theorem.** The fixed fold width and \(u_0\) can be chosen so that
for every fixed \(A<\infty\) and \(q\ge0\), for all sufficiently
large \(N\),
\[
 \boxed{\quad
 \left|\partial_Z^q\!
       \left[e^{-N\mathcal W_\sigma(Z)}\mathcal E_N(Z)\right]\right|
 \le C_{A,q}N^{q-r-1/4}(1+\log N)^{2r}e^{-cNu_s^2},
       \qquad Z\in\mathcal T_{A,N}.
 \quad}
 \tag{5}
\]
The same estimate for \(\partial_Z^q\mathcal E_N\) holds after
restoring \(e^{N\Re\mathcal W_\sigma(Z)}\) on the right.
Constants are uniform for the stated real microscopic parameters
and both parities. In particular the complete first output normal
costs one power of \(N\), and every actual traced normal has
already been retained before this output differentiation.

For real \(|u|\le u_0\), (5) gives the additional Gaussian saving
\(e^{-cNu^2}\). For \(|u|\le A_0N^{-1/2}\), its spectral image
lies in a tube (4) with a fixed \(A\). Thus the \(N^{-1/4}\)
relative fold margin survives on every such shrinking complex
angular disk. No output-derivative lower bound is asserted.

## 2. The original phase and its real output gap

For small real \(t,u\), the central Newton product phase is
\[
 b(v,t)=\int_0^v
       \log\frac{\cos^2(\pi s)-\sin^2(t/2)}
                     {\sin^2(\pi s)}\,ds,\qquad
 F(v;t,u)=b(v,t)+b(v,u).
 \tag{6}
\]
Its unique central critical point \(v_*(t,u)\) continues
holomorphically from \(v_*(0,0)=1/4\); \(F_{vv}(1/4;0,0)=-8\pi\).
The critical value is the original wire phase \(\psi(t,u)\),
with \(\psi(0,0)=2\mathcal I_2\). This is the positive factorial
branch in the local wire source.

For clarity, its derivative can also be obtained directly from
(6). Put \(s_t=\sin(t/2)\), \(s_u=\sin(u/2)\). The critical equation
gives
\[
 \tan(\pi v_*)=
 \frac{\cos(t/2)\cos(u/2)}{\sqrt{1-s_t^2s_u^2}}.
 \tag{7}
\]
Integration of \(b_t\), followed by (7), gives
\[
 \psi_t(t,u)=-\pi^{-1}
       \operatorname{asinh}(\tan(t/2)\cos(u/2)),
 \tag{8}
\]
and the symmetric identity for \(\psi_u\). The branches agree
near zero and continue to the specified two-power saddle.

At that saddle
\(\cos(t_{2\sigma}(u)/2)=
 (1+i\sigma)\sqrt{\cos(u/2)}/2\).
Stationarity and (8) therefore imply
\[
 W_\sigma'(u)
 =-\frac1{2\pi}\operatorname{artanh}(\sin(u/2))
                         -\frac{i\sigma u}{4\pi}.
 \tag{9}
\]
For example this follows by taking the hyperbolic sine of
\(\tfrac12\operatorname{artanh}(\sin(u/2))+i\sigma u/4\);
the two sides agree at zero, fixing the inverse branch.
Consequently, with the original constant retained,
\[
 W_\sigma(u)=W_\sigma(0)
    +\frac{\psi(0,u)-2\mathcal I_2}{2}
                         -\frac{i\sigma u^2}{8\pi}.
 \tag{10}
\]
In particular for real \(u\),
\(\Re W_\sigma(u)=\psi(0,u)/2\).

Use the optimized source saving
\[
 J_*(t)=I_{\delta(t)}((\pi-t)/(2\pi)),\qquad
 \delta(t)=\pi^{-1}\arcsin(\cos(t/2)/\sqrt2).
 \tag{11}
\]
The optimized assembly proves
\(\psi(t,0)-J_*(t)=\mathcal I_2-t^4/(64\pi)+O(t^6)\).
The even analytic phase in (6) has expansion
\[
 \psi(t,u)=2\mathcal I_2-\frac{t^2+u^2}{4\pi}
                              +O(t^4+t^2u^2+u^4).
 \tag{12}
\]
Combining the exact \(u=0\) quartic with (10)--(12), and choosing
small fixed \(t,u\) intervals, gives
\[
 \psi(t,u)-J_*(t)-\Re W_\sigma(u)
                                    \le-c(t^4+u^2).
 \tag{13}
\]
For a seam with \(v=(m+1)/N=\delta(t_s)+O(h)\), the corresponding
anchor comparison is
\[
 \psi(t_s,u)-I_v(1/2)-\Re W_\sigma(u)
                                    \le-c(t_s^2+u^2)+Ch^2 .
 \tag{14}
\]
The raw seam comparison uses \(t_s^4+u^2\) instead.
The literal integer rounding and centered-coordinate shifts
have the same bounded exponential costs as in the pinned assembly.

## 3. Two-variable kernel bounds from the exact sum

Uniformly for real small \(t,u\), midpoint products give
\[
 e_k(-2\cos t)e_k(-2\cos u)
   =\frac{e^{NF(v;t,u)}}{4N^2\sin^2(\pi v)}
                         [1+O_{\rm hol}(h)],\qquad v=k/N,
 \tag{15}
\]
on a fixed central index neighborhood of \(1/4\).
Its maximum is the one in (7), with uniformly negative real
second derivative. The literal shortened sum therefore satisfies
\[
 |L_N(t,Z(u))|\le Ch^{3/2}e^{N\psi(t,u)},\qquad
 |\partial_tL_N(t,Z(u))|
       \le Ch^{3/2}(1+|t|/h)e^{N\psi(t,u)}.
 \tag{16}
\]
The derivative uses \(F_t=O(t)\) uniformly for these real \(u\).
The noncentral absolute logarithmic phases have a fixed gap at
\((t,u)=(0,0)\), and hence on the smaller fixed real rectangle.
Their uniform sine-product mesh bounds and polynomial derivative
losses are absorbed in that gap. This is the same tail argument
as in the direct-cap proof, now with two real variables.

On a small fixed complex height in the traced variable,
the same central expansion gives
\[
 |L_N(t-i\varepsilon H,Z(u))|
 \le Ch^{3/2}e^{N[\psi(t,u)+C H^2]},
 \quad 0\le H\le H_0,\quad \varepsilon=\pm1.
 \tag{17}
\]
Indeed the linear height variation of the real logarithmic phase
vanishes at real \(t,u\); the central curvature and the tail gap
persist for small fixed \(H_0\). This retains the precise
\(h^{3/2}\) prefactor.

Now fix \(Z_s=Z(u_s)\) in (4) and \(|Z-Z_s|\le Ah\).
For all central indices, every factor \(c_a-Z_s\), \(a<k\),
is bounded away from zero by a fixed positive constant.
The exact identity
\[
 \frac{e_k(Z)}{e_k(Z_s)}
       =\prod_{a<k}
          \left(1-\frac{Z-Z_s}{c_a-Z_s}\right)
 \tag{18}
\]
therefore has modulus at most \(e^{C A}\). Every fixed
ordinary \(Z\) derivative costs at most \(C_qN^q\), by
differentiating the product. Equations (16)--(17), and their
traced first derivative where needed, thus hold in this tube
with \(u_s\) on the right and an \(A\)-dependent constant.

The tail estimate is uniform there too. In its logarithmic
products the complex perturbation tends to zero, even at a
factor zero; the limiting absolute logarithmic integral is
uniformly continuous. The mesh upper bound remains
polynomial, by splitting the cells near each displaced zero.
Its fixed exponential gap survives and absorbs every fixed
derivative loss. Thus (18) does not omit any Newton index.

## 4. Repeating the exact physical and contour estimates

The incoming values and normals, the cutoff sequence, and
the raw/anchor baseline jumps do not depend on the outgoing
variable. Insert (16) and (13) into the original physical-jet
sum of the optimized assembly. It is bounded by
\[
 C\Lambda_N^r h^{r+1/4}
             e^{N[\Re W_\sigma(u)-cu^2]} .
 \tag{19}
\]
On every small-height midpoint vertical, use (17). The exact
sampling kernel is still
\((\pi/h)^2\operatorname{sech}^2(H/(2h))\), and its integral
has effective height \(h\). The raw and anchor sums are therefore
\[
 C\Lambda_N^r
       (h^{r+5/4}+h^{r+1})
             e^{N[\Re W_\sigma(u)-cu^2]} .
 \tag{20}
\]
The actual signed chirp, sine weight, parity and cutoff-threshold
counts are unchanged. The derivative in the original trace
continues to be taken before evaluating the physical rows.

The remaining contour parts have a uniform fixed gap at output
zero. For a small fixed real \(u_0\), the outgoing kernel's
half-plane upper bound is uniform on the whole real output
interval, with its complete-output phase as an upper rate.
That fixed gap still lies below
\(\Re W_\sigma(u)-cu^2\), after reducing \(u_0\) and \(c\).
The high outgoing sector has polynomial restricted real trace
on this interval as well.

For completeness, these fixed-gap and high-sector estimates
persist on the tube by an elementary polynomial bound on the
actual outgoing kernels. Their spectral degree is \(O(N)\).
If a polynomial has norm \(M\) on \([-2,2]\), its Chebyshev
coefficients are at most \(2M\), by the cosine integral.
For \(\operatorname{dist}(Z,[-2,2])\le Ah\),
\(|T_\ell(Z/2)|\le e^{C\ell\sqrt{Ah}}\).
Thus continuation costs at most \(CN e^{C_A\sqrt N}\).
It preserves any fixed exponential gap; the high sector
remains subexponential. This bound is used only for those
already separated contributions. The critical terms
(19)--(20) were proved directly from (18), without this loss.
No continuation of a complete-output scalar estimate is used.

The same argument on the tube, using (18) in the critical terms,
gives (19)--(20) with \(u_s\). Since
\(\mathcal W_\sigma(Z)-\mathcal W_\sigma(Z_s)=O_A(h)\),
restoring the actual output phase costs only a constant.
Adding the exact pieces of (3) proves (5) for \(q=0\).

To retain output derivatives, prove this bound on
\(\mathcal T_{A+2,N}\) and apply Cauchy on disks of radius \(h\).
The real reference satisfies
\(|u_s^2-\widetilde u_s^2|\le C h\) for neighboring such disks,
because \(u^2\) is an analytic coordinate at \(Z=-2\).
The reference Gaussian therefore changes by a bounded factor.
Each derivative costs \(h^{-1}\), proving (5) for every fixed
\(q\). The same conclusion for the unnormalized remainder
follows by the product rule and the bounded derivatives of
\(\mathcal W_\sigma\).

## 5. What this does and does not supply for composition

The local wire and actual insertion coefficient are already
holomorphic on a fixed output neighborhood. The result here
controls the critical complementary fold only on the real
interval and shrinking tube (4). Thus it can be combined with
a whole scalar assembly without losing the local coefficient
on \(|u|=O(N^{-1/2})\), while retaining every fixed output
normal with its stated polynomial cost.

There is a precise reason not to infer a fixed disk from this
estimate. At a fixed small imaginary output \(u=ib\),
(10) and the real Taylor coefficients give
\[
 \begin{split}
 &\Re\psi(0,ib)-\mathcal I_2-\Re W_\sigma(ib)\\
 &\hspace{25mm}
       =\frac{b^2}{8\pi}+O(b^4)>0 .
 \end{split}
 \tag{21}
\]
At this output the central Newton factors at real \(t=0\)
are positive; their actual kernel phase is \(\psi(0,ib)\).
The available sharp source saving remains \(\mathcal I_2\).
The resulting fold envelope therefore exceeds the desired
filled action by a fixed quadratic amount. The coherent
error and its original trace may still cancel; (21) is not
an actual-source lower bound or a failure theorem for the
filled packet itself.

The upper-packet composition class requires an actual envelope
on a fixed complex output neighborhood and a whole-boundary
fixed-strip envelope, uniformly on bounded complex microscopic
parameter sets. This theorem has real microscopic parameters
and a shrinking complex output tube. It does not establish
membership in that class or closure under its next filling.
In particular no radius depending on \(N\) is substituted
for the fixed phase chart in that theorem.
For a fixed parent construction, its nonreal saddle has a
fixed positive distance from the real output interval whenever
it is not on that interval. This remains true if the number of
pieces is very large but fixed. Eventually that saddle lies
outside every tube (4), so (5) cannot yet be evaluated there.
The excess in (21) could reflect a competing contribution or
only an overestimate; its actual coefficient has not been
determined here.

## 6. Complete direct sources

* [Optimized critical-fold assembly](research_critical_fold_optimized_block_assembly.md),
  SHA256 d55f935b72ade9b11c2565790da7040d3c7fa1f0fd6d90c1b83ad8be80802b76.
* [Actual cap errors and kernel prefactors](research_critical_fold_actual_trace_error.md),
  SHA256 08a6a612536931629567733d63b2161eca52000f3bea0973c79528c023677bb8.
* [Uniform fold and outgoing high-sector bounds](research_endpoint_uniform_fold_cap.md),
  SHA256 5cdb59337b9e9cccac8bc94fb250106ed6cfc63db7f023ba564e715d8d2900eb.
* [Two-power local wire and original action](research_two_power_shortened_wire_packet.md),
  SHA256 f3ae7c6cad975224f8e93f0de8466707fea22c0ae9d712c437d49053ca7cbd87.
* [The fixed-domain upper composition class](research_microscopic_upper_packet_composition.md),
  SHA256 e72d9cf866330433cb19a2b809f46c3680f944d0af0fab18066622c83f72e911.

The last source is used only to state the precise composition
scope. The new estimates use the actual finite output factors
in (18), the two-variable phase gap, and buffered derivatives
on the explicitly shrinking tube.
