# The actual shrinking-fold trace error at the two-power scale

Private written proof, 16 November 2026.

The original physical trace retains a gain which is lost by a generic
bound for the cardinal interface. The actual error's angular normal is
of size \((|t|+N^{-1/2})e^{-NI(t)}\), with logarithmic coefficients,
and the outgoing low kernel has prefactor \(N^{-3/2}\). Together with
the original trace weight, these bounds make the shrinking fold
trace error smaller than \(N^{-r}e^{N\mathcal I_2}\).

This compares the actual cap to its actual common-anchor baseline.
It does not estimate a growing family of adjacent seams or select the
two-power saddle coefficient. No Fourier frequency gap is used.

## 1. Statement and exact source

Set \(h=N^{-1}\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 C_N(x)=2\cos(2\pi x+\pi h),\quad
 t(x)=\pi-2\pi x-\pi h,\quad x_j=jh,\quad c_j=C_N(x_j).
 \tag{1}
\]
Use the original Newton polynomials
\[
 e_k(C)=\frac{\prod_{a<k}(c_a-C)}{S_k^2},\qquad
 S_k=\prod_{\ell=1}^k2\sin(\pi\ell h),
 \qquad K_N(w,C)=\sum_{k=0}^{D}e_k(w)e_k(C).
 \tag{2}
\]
Fix \(r\ge1\), a real parameter compact \(|\alpha_i|\le A\), and
a fixed signed integer \(n\). Put
\[
 u_i(x)=K_N(2\cosh(\alpha_i h),C_N(x)),\qquad
 B_N(x)=\prod_{i=1}^r u_i(x).
 \tag{3}
\]
For each factor let \(V_i\) be precisely the fold baseline of the
pinned fold theorem: cutoff \(m_f=\lfloor N/4\rfloor\), its original
factorial modes, the coalesced frame at \(\alpha_i=0\), and its actual
two-value anchor at
\[
 j_*=\begin{cases}N/2-1,&N\ {\rm even},\\(N-1)/2,&N\ {\rm odd}.
 \end{cases}
 \qquad B_N^0=\prod_iV_i.
 \tag{4}
\]
There is no freely chosen normal in (4). Define the actual shortened
outgoing kernel at complete output by
\[
 L_N(t)=\sum_{k<\lfloor N/2\rfloor}e_k(-2)e_k(-2\cos t).
 \tag{5}
\]
The crossing's full physical jets are represented by
\[
 R_{N,n}(t)=\mathfrak c_{N,n}e^{inNt^2/(4\pi)},\qquad
 \mathfrak c_{N,n}=e^{\pi i nD^2/(4N)}.
 \tag{6}
\]
In particular its absolute value on the real line is one.

Take a mirrored physical cap \(j_L\le j\le j_R=N-1-j_L\), and
write \(T=\pi-2\pi j_Lh\); its endpoint midpoints correspond to
angles \(T,-T\). If \(f\) is a holomorphic spectral source on this
cap, its restricted original trace is exactly
\[
 \phi_{\rm cap}(f)
   =-\frac{\eta}{2\pi}
       \sum_{j=j_L}^{j_R}
       \partial_x\{\sin t(x)\,f(C_N(x))\}_{x=x_j}.
 \tag{7}
\]
This counts each double spectral root once. At odd levels the
central simple root contributes its value once. Formula (7) also
defines the evaluation on the holomorphic baseline, without making
it a canonical polynomial.

Write
\[
 \mathcal I_2=\frac2\pi\int_0^{\pi/4}\log\cot v\,dv,\qquad
 \mathcal J(t)=\mathcal I_2+
 \frac1\pi\int_0^{\pi/4}
       \log(1-\sin^2(t/2)\sec^2v)\,dv .
 \tag{8}
\]
All constants below are uniform in the stated real parameters and
both parities. Put \(\Lambda_N=(1+\log N)^2\).

**Theorem.** There are \(T_0,C>0\), independent of \(N\), such
that for \(h\le T\le T_0\),
\[
 \begin{split}
 \big|\phi_{\rm cap}\{R_N^n L_N(B_N-B_N^0)\}\big|
 \le{}& C\Lambda_N^r h^{r-1/2}
       (T^3+\sqrt h\,T^2+hT+h^2)\\
 &{}\cdot\exp\{N(\mathcal I_2+CT^4)\}.
 \end{split}
 \tag{9}
\]
Consequently, for any midpoint caps with \(T\asymp N^{-1/4}\),
\[
 \boxed{\quad
 \big|\phi_{\rm cap}\{R_N^n L_N(B_N-B_N^0)\}\big|
 \le C(1+\log N)^{2r}N^{-r-1/4}e^{N\mathcal I_2}
       =o(N^{-r}e^{N\mathcal I_2}).
 \quad}
 \tag{10}
\]
For \(r=0\) the difference is identically zero. The theorem concerns
complete output in (5); no output-derivative version is asserted.
The signed crossing remains unchanged throughout the proof.

## 2. Refined errors from the actual recurrence

We first prove, at every physical row in a fixed fold neighborhood,
\[
 \begin{split}
 |u_i-V_i|&\le Ch\Lambda_N e^{-N\mathcal J(t_j)},\\
 |\partial_x(u_i-V_i)|&\le
       C\Lambda_N(|t_j|+\sqrt h)e^{-N\mathcal J(t_j)},\\
 |u_i|+|V_i|+|V_i'|&\le Ch\Lambda_N .
 \end{split}
 \tag{11}
\]
These bounds concern the actual full angular jets, including the
even last normal. At the odd simple color the zero angular normal
is retained but is not interpreted as extra spectral data.

Use the regular divided-color state and mode frame
\[
 \mathcal V_f=
 \binom{f(x)}{[f(x)-f(x-h)]/[C_N(x)-C_N(x-h)]},
 \qquad \mathcal F=(\mathcal V_{H_0},\mathcal V_{H_1}).
 \tag{12}
\]
The reflected source and fold theorems give uniformly bounded
\(\mathcal F,\mathcal F^{-1}\) and their fixed derivatives through
the fold. Their source-specific coefficient calculation gives
\(\|\mathbf a_*\|\le Ch(1+\log N)\). Thus
\(V=H\mathbf a_*\) and every fixed derivative of \(V\) are bounded
by \(Ch\Lambda_N\).

Let \(r_V=(\mathscr J_N-w)V\). The literal last-summand expansion
in the fold theorem, including its \(h\) prefactor and the
coalescence at zero, gives
\[
 |r_V|\le Ch^2\Lambda_N E(t),\qquad
 |r_V'|\le Ch^2\Lambda_N(1+|t|/h)E(t),\qquad
 E(t)=e^{-N\mathcal J(t)}.
 \tag{13}
\]
Here and below \(x\) and \(t\) derivatives differ by the fixed
factor \(-2\pi\). To verify the derivative estimate explicitly,
differentiate the last-summand expression
\(h^{2z+2}A_z(x,m_f/N)e^{-NI_{m_f/N}(x)}\), multiplied by the
bounded lowering coefficient and the actual anchor. Its amplitude
has bounded fixed spatial derivatives; coalescence introduces
at most logarithms of \(N\). On this neighborhood
\(I_{m_f/N}'(x)=O(|t|+h)\). The literal cutoff rounding and the
center shift change \(N I\) by \(O(t^2+|t|+h)\), uniformly bounded.
This proves (13) with the displayed \(\Lambda_N\), rather than
an unspecified power of \(N\). The two raw mode residuals and
their first derivatives also satisfy a polynomial times \(E\)
bound with explicit powers of \(h^{-1}\) and logarithms; only
their exponential smallness will be needed in a quadratic error.

For completeness, put \(s_z=2\sin(\pi hz)\),
\(c_0=2\cos(\pi h)\), \(w=2\cosh(\alpha h)\), and
\[
 A_N=\frac{s_{Nx+1}^4}{s_{2Nx+1}s_{2Nx+2}},\qquad
 B_N=\frac{s_{Nx}^4}{s_{2Nx}s_{2Nx+1}},\qquad
 \mathscr J_N f=(c_0+A_N+B_N)f-A_Nf(x+h)-B_Nf(x-h).
\]
The exact regular transfer, with apparent poles canceled, is
\[
 \mathcal V_f(x+h)=T^\sharp(x)\mathcal V_f(x)
                       -\mathbf b(x)(\mathscr J_N-w)f(x),
 \quad
 \mathbf b=\binom{1/A_N}{b^\sharp},
 \tag{14}
\]
\[
 b^\sharp=-\frac{\sin(2\pi x+\pi h)}
                 {16\sin(\pi h)\sin^4\pi(x+h)},\qquad
 q^\sharp=\left(\frac{\sin\pi x}{\sin\pi(x+h)}\right)^4,
 \tag{15}
\]
\[
 T^\sharp=
 \begin{pmatrix}
 1+(c_0-w)/A_N&q^\sharp[C_N(x+h)-C_N(x)]\\
 (c_0-w)b^\sharp&q^\sharp
 \end{pmatrix}.
 \tag{16}
\]
Both \(T^\sharp\) and its inverse are \(I+O(h)\) on the fixed
neighborhood. Also
\[
 \|\mathbf b(x)\|\le C|t|/h,\qquad
 \|\mathbf b'(x)\|\le C/h .
 \tag{17}
\]
In particular no artificial division by the last color separation
is made. The formula for \(1/A_N\) has the same zero at \(t=0\)
and obeys (17).

The actual ordinary kernel residual is
\[
 r_K=-\frac{P_N(w)P_N(C_N(x))}
                  {N^4(C_N(x)-c_0)},\qquad
 P_N(C)=2T_N(C/2)+2,\qquad
 P_N(C_N(x))=4\sin^2(\pi Nx),
 \tag{18}
\]
where \(T_N\) is the Chebyshev polynomial.
Thus \(r_K=r_K'=0\) at every physical row in this neighborhood.
The error state in (14) has zero initial state at the actual
anchor (4), and its nodal forcing is \(\mathbf b\,r_V\).
Its transfer products, in either direction, are uniformly bounded.

We record the elementary estimates used to sum this forcing.
For small fixed \(T_0\), \(-\mathcal J'(s)\asymp s\) on
\(0<s<T_0\). On a mesh whose spacing is between fixed positive
multiples of \(h\), with endpoints
altered by at most \(Ch\),
\[
 \sum_{|s_\ell|\le t+Ch}h(|s_\ell|+h)E(s_\ell)
                       \le Ch E(t),
 \tag{19}
\]
\[
 \sum_{|s_\ell|\le t+Ch}(h+s_\ell^2)E(s_\ell)
                       \le C(t+\sqrt h)E(t).
 \tag{20}
\]
For \(t\le\sqrt h\) these follow by counting the \(O(t/h+1)\)
terms and comparing \(E(s)\) to \(E(t)\). For \(t>\sqrt h\),
split at \(t/2\), use
\(\mathcal J(s)-\mathcal J(t)\ge c t(t-s)\) on the upper half,
and sum the resulting geometric series. The lower half has
Gaussian suppression. This proves (19)--(20) with constants
uniform through \(t=0\).
Equations (13)--(19) prove that the error state, and hence its
value and coefficient vector, have bound \(Ch\Lambda_NE(t_j)\).

Here is the separate normal argument. Write
\(\mathbf a=\mathcal F^{-1}\mathcal V_u\),
\(\mathbf e=\mathbf a-\mathbf a_*\), and
\(\ell=\mathcal F(x+h)^{-1}\mathbf b\). If \(\mathbf r\) is the
row of raw mode residuals, the exact coefficient equations are
\[
 \mathbf e_{j+1}=(I+M_j)\mathbf e_j+\ell_jr_V(x_j),\qquad
 M=\ell\mathbf r ,
 \tag{21}
\]
\[
 \mathbf e_{j+1}'=(I+M_j)\mathbf e_j'
                    +M_j'\mathbf e_j+(\ell r_V)'(x_j).
 \tag{22}
\]
Equation (22) follows by differentiating before evaluation and
using both vanishings in (18). Reflection gives exactly
\(\mathbf e(1-x)=\mathbf e(x)\).

By (13), (17) and the bounded frame,
\[
 |(\ell r_V)'(x_j)|
                   \le C\Lambda_N(h+t_j^2)E(t_j).
 \tag{23}
\]
The term \(M_j'\mathbf e_j\) is exponentially smaller than
(23), with harmless powers and logarithms, because the already
proved error bound and the raw residual each contain \(E\).
Propagate (22) from \(j\) to \(N-j\). The product of \(I+M\)
is \(I+O(e^{-cN})\) on the fixed fold neighborhood. Reflection
negates the derivative at the other end, so the coefficient of
\(\mathbf e_j'\) is \(2I+O(e^{-cN})\), a uniform unit.
Summing (23) by (20) proves
\[
 \|\mathbf e_j'\|\le
                  C\Lambda_N(|t_j|+\sqrt h)E(t_j).
 \tag{24}
\]
Multiplication by the bounded row \(H\), and its derivative, gives
the first two assertions of (11). The third follows from the
baseline bound and the exponentially small value error.
This argument retains the independent normal throughout.

By the product rule, (11) implies for
\(\Delta B=B_N-B_N^0\)
\[
 |\Delta B|\le Ch^r\Lambda_N^r E(t_j),\qquad
 |\partial_t\Delta B|\le
 Ch^{r-1}\Lambda_N^r(|t_j|+\sqrt h)E(t_j).
 \tag{25}
\]

## 3. The real outgoing kernel with its exact power of \(N\)

Uniformly for real \(|t|\le T_0\),
\[
 |L_N(t)|\le Ch^{3/2}e^{N\psi(t,0)},\qquad
 |L_N'(t)|\le Ch^{3/2}(1+|t|/h)e^{N\psi(t,0)} .
 \tag{26}
\]
We give the product proof, since a generic polynomial prefactor
would not suffice here.

For \(v=k/N\) in a fixed neighborhood of \(1/4\), midpoint
Euler summation in the numerator of (2), and the exact factorial
expansion for \(S_k\), give
\[
 e_k(-2\cos t)
  =\frac{e^{Nb(v,t)}}{2N\sin(\pi v)}
                      (1+O_{\rm hol}(h)),
 \tag{27}
\]
\[
 b(v,t)=\int_0^v
 \log\frac{\cos^2(\pi s)-\sin^2(t/2)}{\sin^2(\pi s)}\,ds .
 \tag{28}
\]
All numerator factors are positive on this central neighborhood
for small real \(t\), and are units on a fixed complex enlargement;
the derivative version of (27) follows there as well.
In particular the prefactor of \(e_k(-2)\) is \(N^{-1}\),
not \(N^{-3/2}\).

Put \(\Phi(v,t)=b(v,t)+b(v,0)\). It has a unique central maximum
\(v_*(t)\), with uniformly negative second derivative, specified by
\[
 \cos^2(\pi v_*(t))
                    =\frac1{1+\cos^2(t/2)} .
 \tag{29}
\]
The maximum is \(\psi(t,0)\): at \(t=0\) its value is
\(2\mathcal I_2\), and differentiating it gives
\[
 \partial_t\Phi(v_*(t),t)
  =-\pi^{-1}\operatorname{artanh}(\sin(t/2))
  =-\pi^{-1}\operatorname{asinh}(\tan(t/2)).
 \tag{30}
\]
These are the normalization and derivative of the original
outgoing phase. Moreover \(\Phi_t(v,t)=O(t)\) on the central
neighborhood. Multiplying (27) at \(t\) and zero, and summing
the Gaussian bound
\(\Phi(v,t)\le\psi(t,0)-c(v-v_*(t))^2\), proves (26)
for the central indices: each term has prefactor \(N^{-2}\)
and their effective number is \(O(\sqrt N)\).

Here is a uniform tail justification including numerator zeros.
For a shifted midpoint sine product on a real interval, its
logarithm is bounded above by the corresponding logarithmic
integral plus \(C\log N\), uniformly in the shift. Split the
mesh into the at most two cells touching a sine zero and the
remaining cells. The touching-cell excess is bounded above
after scaling the cell by \(h\); on the other cells the
second-derivative error is bounded by a constant times the
inverse square of their distance in mesh units, which is
summable. The weaker \(C\log N\) bound therefore suffices.
The denominator \(S_k\) has the matching integral with
\(O(\log N)\) error, also at the ends.

Apply this to the two cosine products in the numerator of (2).
The resulting absolute logarithmic phase is continuous, uniformly
as \(t\to0\), on \(0\le v\le1/2\); this also follows by
integrating the local \(\log|s-s_0|\) singularities.
At \(t=0\) it is \(2b(v,0)\), whose unique maximum is at \(1/4\).
Hence, outside the chosen central neighborhood, all tail terms
are bounded by a polynomial times \(e^{N(2\mathcal I_2-c)}\)
for sufficiently small fixed \(T_0\). The same is true of
their sum. Markov's inequality for its polynomial in
\(C=-2\cos t\), on a slightly larger fixed real color interval,
gives the same bound with a polynomial loss for its derivative.
Shrinking \(T_0\) if necessary, this is exponentially below
both bounds in (26). This proves (26) for the literal sum (5)
at both parities, without adding the odd middle term.

## 4. Summing the original trace

The fixed fold action and the actual outgoing phase satisfy
\[
 \psi(t,0)-\mathcal J(t)
       =\mathcal I_2+\frac{t^4}{64\pi}+O(t^6)
       \le\mathcal I_2+Ct^4.
 \tag{31}
\]
This is the fixed-cutoff expansion; replacing it by the optimized
action would give the wrong quartic sign.
Set
\[
 g(x)=\sin t(x)\,R_{N,n}(t(x))L_N(t(x))\Delta B(x).
 \tag{32}
\]
The exact bounds \(|R_{N,n}|=1\) and
\(|\partial_tR_{N,n}|\le C_n|t|/h\), together with (25)--(26),
give at each physical point of the cap
\[
 |g'(x_j)|\le
 C\Lambda_N^r h^{r+1/2}
 (h+t_j^2+|t_j|\sqrt h)
          e^{N(\mathcal I_2+CT^4)} .
 \tag{33}
\]
Thus no normal was replaced by a values-only bound. In particular
the \(\sin t\) factor in the trace multiplies the actual
\((|t|+\sqrt h)\) normal scale.

The mesh spacing in \(t\) is \(2\pi h\). Summing the elementary
polynomial in (33), including its endpoint terms, gives
\[
 \sum_{j=j_L}^{j_R}(h+t_j^2+|t_j|\sqrt h)
 \le C h^{-1}(hT+T^3+\sqrt h\,T^2+h^2).
 \tag{34}
\]
Equations (7), (33) and (34) prove (9), and substitution of
\(T\asymp h^{1/4}\) proves (10). This is an absolute estimate
of the actual coherent cap difference, not a stationary-phase
estimate or a bound on separately assigned Fourier sectors.

The baseline trace on the same cap remains to be moved along
its exact contours with all endpoint currents retained. The
theorem supplies no estimate for the difference of baselines
on an increasing number of adjacent windows. It also supplies
no nonzero two-power local coefficient or arbitrary composed
source bound. Its contribution is the quantitative removal
of this actual shrinking-cap error at the critical scale.

## 5. Direct sources

The complete direct sources are:

* [Uniform fold cap](research_endpoint_uniform_fold_cap.md),
  SHA256 5cdb59337b9e9cccac8bc94fb250106ed6cfc63db7f023ba564e715d8d2900eb.
  This supplies the actual fold anchor, real-parameter coefficient
  and last-residual normalizations, full trace multiplicity, and
  the original fixed-cutoff action.
* [Reflected sharp normal connection](research_reflected_endpoint_sharp_normal_connection.md),
  SHA256 a8a379d7b492d7d2487de3c1397408478f66242f153ac0cab8eb3d224f226916.
  This supplies the exact ordinary source, regular divided-color
  transfer, and differentiated coefficient reflection.
* [Exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md),
  SHA256 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.
  Its normalized sine factorial expansion gives the precise
  \(N^{-1}\) row prefactor used in (27).

The new source estimate is (11), followed by the original physical
trace sum (33)--(34). It does not require a new summation-by-parts
identity and does not assert a gap in the repair's frequency support.
