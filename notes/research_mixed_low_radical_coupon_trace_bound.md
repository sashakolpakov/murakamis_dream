# Mixed low and radical half-charge coupons

Put \(N\ge2\), \(D=N-1\), \(m=\lfloor N/2\rfloor\),
\(L=D-m\), and retain the original Newton data
\[
 c_a=2\cos((2a+1)\pi/N),\quad
 S_j=\prod_{\nu=1}^j2\sin(\nu\pi/N),\quad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z),
 \]
\[
 A=e_L,\quad B=e_{L+1},\quad s_m=2\sin(m\pi/N),\quad
 K_N(z,w)=\sum_{j=0}^D e_j(z)e_j(w).
 \tag{1}
\]
The trace and signed crossing powers are the original
full-Hermite operations. Alongside the low coupons of [A],
define their radical counterparts
\[
 \mathcal C_{r,n,N}=\phi_N^{(z)}
       \left[R(z)^n A(z)\prod_{i=1}^rK_N(z,\zeta_i)\right],
 \qquad
 \mathcal D_{r,n,N}=\phi_N^{(z)}
       \left[R(z)^n B(z)\prod_{i=1}^rK_N(z,\zeta_i)\right].
 \tag{2}
\]
Here \(r\ge1,n\in\mathbb Z\) are fixed; outside variables
remain ordinary. Use the physical angles and multiplicities
\[
 J=\lfloor(N-1)/2\rfloor,\qquad
 \tau_a=\arccos(-c_a/2),\quad g_a=1-\cos\tau_a,\qquad
 \mu_a=\operatorname{mult}_{c_a}P_N .
 \tag{3}
\]
Every \(\mu_a=2\), except for the odd simple node \(c_m=-2\),
where \(\mu_m=1\) and \(g_m=0\).

## 1. The radical coupon has the same half-charge action

For \(r+|n|>1\), retain precisely the complete branch of [A]:
\[
 nt_*+2ir\operatorname{asinh}\tan(t_*/2)=\pi,\qquad
 \Im t_*<0,\quad|\Re t_*|<\pi,
 \]
\[
 \mathcal S_{r,n}
 =r\Psi(t_*)+\frac{int_*^2}{4\pi}-\frac{it_*}{2},
 \quad M_{r,n}=\Re\mathcal S_{r,n},\quad
 \mathfrak A=\frac{r\sec(t_*/2)-in}{2\pi}.
 \tag{4}
\]
Here \(\Psi\) is the original complete edge phase and
\(\Re\mathfrak A>0\). Let
\[
 \chi_N=e^{\pi iD^2/(4N)},\qquad
 K_N^{\rm low}(-2\cos t,-2)=e^{N\Psi(t)+E_N(t)}.
 \]
The logarithm and its \(O(\log N)\) derivative bounds on
the complete contour neighborhood are those of [A].

**Theorem.** For every fixed multi-index \(\nu\), there are
\(c,C_\nu>0,A_\nu\) such that, at all physical outside
assignments and all sufficiently large levels,
\[
 |(\partial^\nu\mathcal D_{r,n,N})(c_{b_1},\ldots,c_{b_r})|
 \le C_\nu N^{A_\nu}
 \exp\left\{NM_{r,n}
        -cN\sum_{i:\nu_i=0}g_{b_i}\right\}.
 \tag{5}
\]
Its complete value has the asymptotic
\[
 \mathcal D_{r,n,N}(-2,\ldots,-2)
 =\chi_N^n\frac{\sqrt{2\pi N}}{\pi\sqrt{\mathfrak A}}\,
       b^B_N(t_*)\,e^{N\mathcal S_{r,n}+rE_N(t_*)}(1+o(1)),
 \tag{6}
\]
with the same square-root convention as [A], and
\[
 b^B_N(t)=
 \begin{cases}
 -2\sin t\sin(t/2)/s_m^2,&N\text{ odd},\\
 2i\sin t/s_m^2=(i/2)\sin t,&N\text{ even}.
 \end{cases}
 \tag{7}
\]
All displayed factors at \(t_*\) are nonzero; the factor
outside \(e^{N\mathcal S_{r,n}}\) has upper and lower
polynomial bounds. Thus this complete local coupon has
rate \(M_{r,n}\), through both parities.

The remaining pair \((r,n)=(1,0)\) is exactly
\(\mathcal D_{1,0,N}=e_{m-1}\). It satisfies (5) at
rate \(M_{1,0}=0\), but is assigned no half-charge saddle.

## 2. Exact source and contour normalization

Since \(B=e_{D-(m-1)}\), the radical formula [H] gives
the ordinary polynomial identity
\[
 \mathcal D_{r,n,N}(\boldsymbol\zeta)
 =\sum_{a=0}^{m-1}b_{m-1,a}R(c_a)^n
                           \prod_{i=1}^rF_{a,N}(\zeta_i),
 \quad F_{a,N}(w)=K_N(c_a,w),
 \tag{8}
\]
\[
 b_{u,a}=(-1)^{u+a}
 \frac{[2\sin((2a+1)\pi/N)]S_u^2}
                {S_{u-a}S_{u+a+1}},\qquad |b_{u,a}|\le2.
 \]
It retains the original surviving normal. At \(N=2\) it
is the direct identity \(b_{0,0}=1\).
Since \(F_{a,N}\) has degree \(a\), each outside degree
in (8) is at most \(m-1\).

The exact Newton multiplier is
\[
 B(z)=p_N(z)A(z),\qquad
 p_N(z)=\frac{c_L-z}{s_m^2},\qquad
 c_L=\begin{cases}-2,&N\text{ odd},\\
                  c_*=-2\cos(\pi/N),&N\text{ even}.
       \end{cases}
 \tag{9}
\]
Here \(s_{L+1}=s_m\) at both parities. The radical \(B\)
annihilates every high factor in the traced algebra.
Consequently (2) equals the low-kernel product with the
central factor \(A p_N\). At odd levels \(B e_m=0\)
as well, although retaining that low term in the analytic
product is permitted. All these reductions concern only
the internally traced variable.

Apply the exact original adapter in [A, Section 2] to
\(p_N f_N\), where \(f_N(z)=\prod_iK_N^{\rm low}(z,\zeta_i)\).
This is an application to the entire function, including
its central normal, not an inference from an upper bound
for the unmultiplied coupon. In particular \(p_N(c_*)=0\)
at even levels while its derivative remains in the adapter.
At odd levels \(p_N(-2)=0\), so the simple-node term is
killed exactly.

The normalization can also be seen directly. Put
\(\epsilon_N=(-1)^m\) and let \(Q_d\) be the monic polynomial
of the \(m\) double nodes:
\[
 Q_d(z)=
 \begin{cases}
 U_m(z/2)-U_{m-1}(z/2),&N\text{ odd},\\
 2T_m(z/2),&N\text{ even}.
 \end{cases}
 \]
The literal polynomials satisfy
\[
 B=
 \begin{cases}
 -\epsilon_N(z+2)Q_d/(Ns_m^2),&N\text{ odd},\\
 \epsilon_NQ_d/(2N),&N\text{ even}.
 \end{cases}
 \]
Using \(P_N=(z+2)Q_d^2\) odd and \(P_N=Q_d^2\) even
in the original residue trace therefore gives
\[
 \phi_N(Bh)=
 \begin{cases}
 -\epsilon_NN s_m^{-2}\displaystyle\sum_{a<m}
                          h(c_a)/Q_d'(c_a),&N\text{ odd},\\
 -\epsilon_NN/2\displaystyle\sum_{a<m}
                          h(c_a)/Q_d'(c_a),&N\text{ even}.
 \end{cases}
 \tag{10}
\]
Only values remain, so the actual crossing values may be
represented here by
\(\chi_N^n e^{inNt^2/(4\pi)}\) at \(z=-2\cos t\).

On the midpoint rectangle supplied by [A, Section 4], the
identities
\[
 Q_d(-2\cos t)=
 \begin{cases}
 \epsilon_N\sin(Nt/2)/\sin(t/2),&N\text{ odd},\\
 2\epsilon_N\cos(Nt/2),&N\text{ even}
 \end{cases}
 \]
turn the selected part of (10) into its paired lower integrals
\[
 \begin{cases}
 \displaystyle-\frac{2N\chi_N^n}{\pi s_m^2}
 \int\frac{\sin t\sin(t/2)f_N(-2\cos t)
            e^{inNt^2/(4\pi)-iNt/2}}{1-e^{-iNt}}\,dt,
 &N\text{ odd},\\[2mm]
 \displaystyle\frac{iN\chi_N^n}{2\pi}
 \int\frac{\sin t\,f_N(-2\cos t)
            e^{inNt^2/(4\pi)-iNt/2}}{1+e^{-iNt}}\,dt,
 &N\text{ even}.
 \end{cases}
 \tag{11}
\]
The path is \([-T_N-iH_*,T_N-iH_*]\). The paired vertical
sides and the omitted physical values of (10) are retained.
For (11), the spectral residue pulls back with factor
\(1/(4\pi i)\), counting both angular preimages; the
odd angular integrand makes the two horizontal sides add.
The odd point \(t=0\) is regular in this double-node sampler.

## 3. Bounds, Gaussian, and the exceptional polynomial

The contour argument in [A, Sections 4--5] has the following
multiplier consequence. A fixed-degree central polynomial
whose fixed derivatives are uniformly bounded on that rectangle
and the physical interval preserves every complementary upper
bound. Apply the exact adapter to the multiplied function:
its contour integrands and omitted values acquire that multiplier,
while its central normal is still evaluated by the same adapter.
If the multiplier is bounded away from zero at the complete
saddle, the leading Gaussian acquires precisely its saddle value.
This follows directly from the strict complementary gaps and
the local Gaussian window used there. It includes the full
vertical sides and the nonconstant denominator parts.
The linear \(p_N\) in (9) meets these bounds uniformly.

At complete outside values use
\(f_N(-2\cos t)=e^{rN\Psi(t)+rE_N(t)}\).
The stationary phase and horizontal orientation are unchanged.
The old amplitude in [A, (8)] is multiplied by
\(p_N(-2\cos t_*)\), giving exactly (7) and hence (6).
No even high correction remains, since multiplication by \(B\)
has already killed it. The factors in (7) are nonzero because
\(\Im t_*<0\), \(|\Re t_*|<\pi\), and \(t_*\ne0\).
At \(n=0,t_*=-iH_*\), both are positive.
For negative \(n\), coefficient conjugation and
\(t_{r,-n}=-\overline{t_{r,n}}\) give the same formulas.

At physical outside values the actual row-ratio estimate in
[A, Section 7] supplies
\(e^{-cN\sum_i g_{b_i}}\) on the entire selected contour.
The bounded central multiplier does not alter it. The
omitted physical values retain their fixed gap; decreasing
\(c\) makes their gap pay the at most \(2r\) total loss.
This proves (5) for values without differentiating a
sampled estimate.

For a hit set \(I=\{i:\nu_i>0\}\), interpolate only those
slots at all distinct physical nodes, dropping their losses.
This is exact because (8) has degree at most \(m-1\), and
there are \(m\) nodes even and \(m+1\) odd. Their cardinal
interpolation has the polynomial Lebesgue bound used in
[A, Section 7]. Tensor interpolation followed by tensor
Markov inequalities gives every fixed hit derivative,
retaining all unhit losses. There is no even correction in
this step. It proves (5) and also a polynomial-times-
\(e^{NM_{r,n}}\) bound for the entire real outside cube
and its fixed ordinary derivatives.

For the exception, Frobenius duality gives exactly
\(\mathcal D_{1,0,N}=e_{m-1}\). Its physical values vanish
unless \(a=m-1\), or also \(a=m\) at odd levels. All
these remaining angles satisfy \(\tau_a\le2\pi/N\).
The last Newton ratio and the complete values in [A, (11)]
give
\[
 e_{m-1}(-2)=
 \begin{cases}
 [4\sin^2(\pi/(2N))]^{-1},&N\text{ odd},\\
 [N\sin^2(\pi/(2N))]^{-1},&N\text{ even}.
 \end{cases}
 \tag{12}
\]
They are at most \(N^2/4,N\), respectively. Every surviving
double-node value is bounded by this complete value, directly
from the positive Newton factors. The same degree-\(m-1\)
interpolation and Markov bounds give polynomial ordinary
derivatives. Since \(Ng_a=O(N^{-1})\) on its value support,
(5) holds with rate zero and any fixed positive \(c\).

## 4. Mixed products and the literal cutoff forcing

Take a fixed finite collection of \(\mathcal C\)- and
\(\mathcal D\)-coupons, with arbitrary identifications of
their ordinary outside slots to variables \(z_v\), \(v\in V\).
Let \(q_v\) count all slot occurrences and \(T_N\) be their
product. Give either type with parameters \((r,n)\) the
action \(M_{r,n}\), with \(M_{1,0}=0\), and sum these
actions as \(\mathcal M\). Equations (5) and [P] give
\[
 |\partial^\alpha T_N(c_{\mathbf a})|
 \le CN^A e^{N\mathcal M-cN\sum_v(q_v-\alpha_v)_+g_{a_v}},
 \qquad \alpha_v\in\{0,1\}.
 \tag{13}
\]
For an arbitrary joint ordinary exterior \(E_N(\mathbf z;\xi)\),
define the same full-jet norm as [P],
\[
 \|E_N\|_{N,c,\mathbf q}
 =\max_{\substack{\mathbf a\\0\le\beta_v<\mu_{a_v}}}
 |\partial^\beta E_N(c_{\mathbf a};\xi)|
 e^{-cN\sum_v(q_v-1+\beta_v)_+g_{a_v}}.
 \tag{14}
\]
The full original trace with any fixed signed powers \(h_v\)
then satisfies
\[
 \left|\phi_N^{\otimes V}
       [E_N\prod_vR(z_v)^{h_v}T_N]\right|
 \le CN^{A'}e^{N\mathcal M}\|E_N\|_{N,c,\mathbf q}.
 \tag{15}
\]
Indeed each derivative of the trace hits the exterior, a
crossing, or one coupon occurrence. If the exterior takes
order \(\beta_v\), at most \(1-\beta_v\) coupon slots can
be hit. This proves the weight in (14), exactly as in [P],
with the original signed normal costs and odd simple value
unchanged. All free variables remain ordinary.

Finally Newton multiplication and
\(\mathscr L e_j=c_je_j-s_j^2e_{j-1}\) telescope to
\[
 (w-\mathscr L^{(z)})K_N^{\rm low}(z,w)
                     =-s_{L+1}^2A(z)B(w).
 \tag{16}
\]
After attaching \(r\) full kernels to the tail and \(s\)
to the head, their two original traces give exactly
\(-s_{L+1}^2\mathcal C_{r,n,N}\mathcal D_{s,p,N}\).
Thus the action in its mixed-jet and further trace bound
is \(M_{r,n}+M_{s,p}\), since \(s_{L+1}^2\le4\).

The complete local asymptotic (6) does not make these
mixed products or their final traces nonzero. Their
particular exterior norm remains unestimated, and the
action sum is not identified with a parent filled volume.
No homogeneous low-source remainder or selected global
cycle is controlled by (15).

## Direct sources

- A: [The original multi-leg half-charge coupon](research_multileg_half_charge_source_bound.md),
  SHA256 df85063947dc52c876d1cb810208e4da725517b7556661e3ddb21a3de7f0f8d2.
  The exact adapter, complete branch, original contour and all
  complementary bounds, low logarithmic error and physical row decay.
- H: [Full high Newton radical contraction](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03.
  The exact radical value formula, signed phases and bounded coefficients.
- P: [Products of half-charge coupons](research_half_charge_coupon_product_trace_bound.md),
  SHA256 447dbd477941526ce56ddef6767715636401f621d7aaf1481bc9b9c22fa02ffe.
  The low mixed-jet bounds and exceptional polynomial, repeated-slot
  rule, and full original trace with its weighted exterior.
