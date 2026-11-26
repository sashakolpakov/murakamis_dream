# All real ordinary colors on the complete complementary contour

Research deduction, 7 November 2026. The complete complementary
contour of the original ordinary three/four source has the same
strict gap for both ordinary colors throughout their real periods.
The proof keeps the whole first cap and every complete physical
terminal row. Its only extension of an endpoint estimate is from
the unit circle to the closed unit disk, using the very same finite
coefficient inequalities. A fixed part of the source-region gap
then supplies explicit angular losses at both endpoints.
No numerical evaluation or certificate replay is used.

## 1. Source, reference, and the contour being estimated

Use precisely the functions and normalization in
[complementary-contour completion](research_mixed_three_four_complementary_contour_completion.md):
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{N-1}
        \frac{H_N(w,r^{-j})p_j(X)}{P_j},\\
 V_{1,N}(w,X)&=\sum_{i=0}^{N-1}
        \frac{X^{-i}p_i(X)}{P_i^2}U_{1,N}(w,r^i),\\
 Z_{34,N}(w_L,w_R)&=\kappa_N^3N^2\int_0^1
      U_{0,N}(w_L,e^{-2\pi ia})V_{1,N}(w_R,e^{-2\pi ia})\,da.
\end{split}                                                     \tag{1}
\]
Here \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and \(|\kappa_N|=1\).
Every \(H_N\) and \(U_1\) in (1) is its complete original
polynomial, including every Newton term and every ordinary normal.

Let \(M\) and \(c\) be the unchanged complete-color action
and incoming reference height. The original source identification
and the single saved result used by complementary-contour completion
give
\[
                       M>27/10,\qquad -7/200<c<0.
                                                               \tag{2}
\]
This is the same saved artifact with SHA256
`fbd429caab1fe76764f35b2e1beaaa5e4a273038d810acabe708d5644ea82b70`;
no new value is obtained here.

The fixed contour \(\Gamma_+\) runs vertically from
\(1/2+ic\) to \(1/2\), then along the real interval to one.
In particular \(X=e^{-2\pi ia}\) satisfies \(|X|\le1\)
everywhere on this contour. The contour is kept fixed as the real
ordinary colors vary; no far-color critical point is introduced.

## 2. The whole first cap on the closed disk and far half

Put \(S_j=|P_j|\). The all-real-color endpoint source theorem
in [terminal real-color decay](research_mixed_terminal_real_color_decay.md),
equations (4)--(5), gives
\[
 |H_N(w,r^{-j})|\le C_I N^{B_I}e^{Nh(j/N)},
 \quad h(e)=J(e)+\lambda(e),\quad j/N\in I\Subset(0,1),
 \quad -2\le w\le2,
                                                               \tag{3}
\]
where \(\lambda(e)=\Re S(e)\) is the original complete-color
endpoint action. The estimate concerns the whole coefficient.
It drops its favorable compact-index angular loss.

The two physical private ends must be checked separately from (3).
The [real-circle endpoint theorem](research_mixed_cap_real_circle_index_ends.md)
supplies the exact finite inequalities, for \(j=N-1-m\),
\[
 \begin{split}
 \frac{p_j(X)}{P_j}
   &=\sum_{\ell=0}^j
      \frac{(-1)^\ell r^{\ell(\ell+1)/2}X^\ell}
                          {P_\ell P_{j-\ell}},\\
 \frac1{S_\ell S_{j-\ell}}
   &=\frac{S_{m+\ell}}{N S_\ell}\le\frac{2^m}{N},\\
 |H_N(w,r^{-j})|
   &\le\frac{2^m}{S_m}\sum_{\ell=0}^{j}|e_\ell(w)|.
 \end{split}                                                   \tag{4}
\]
The coefficientwise proof of that theorem uses only
\(|X|^\ell\le1\), so its consequence
\[
                        |p_j(X)|/S_j\le2^m
                                                               \tag{5}
\]
holds on the entire closed disk \(|X|\le1\), not just its
boundary. The exact low-index proof likewise uses
\(|p_j(X)|\le2^j\), which holds on that same disk.
The uniform all-color Newton bound is
\(\sum_\ell|e_\ell(w)|\le\operatorname{poly}(N)e^{Nb_2}\),
with \(b_2<73/125<3/5\).

Consequently the original choice of a sufficiently small fixed
endpoint width, reduced if necessary, gives
\[
 \sum_{\substack{0\le j<N\\ j/N\le\delta_0\ \mathrm{or}\ j/N\ge1-\delta_0}}
       \frac{|H_N(w,r^{-j})|\,|p_j(X)|}{S_j}
       \le C N^B e^{3N/5},\qquad |X|\le1,\quad -2\le w\le2.
                                                               \tag{6}
\]
This preserves exactly the old reflected-factorial and low-Newton
supports, both parities and every numerator zero. In particular
it does not extrapolate (3) to either physical endpoint.

For the remaining compact private indices, write
\(X=e^{-2\pi i(x+ih)}\), \(1/2\le x\le1\),
\(c\le h\le0\), and \(R=e^{2\pi h}\le1\).
The zero-safe upper rate of the numerator is
\[
 I_{x,R}(e)=\int_0^e\log|1-Re^{-2\pi i(x+u)}|\,du.
                                                               \tag{7}
\]
The exact radial comparison in
[the far-half cap extension](research_mixed_three_four_far_half_cap_radial_extension.md),
equation (9), proves
\[
 I_{x,R}(e)\le
 \begin{cases}
       -J(1/2-e),&e\le1/2,\\
       J(e),&e\ge1/2.
 \end{cases}                                                   \tag{8}
\]
It is a color-independent product inequality. Combining it with
(3) and the uniform sine-product denominator gives the original
compact row rate \(\lambda(e)+I_{x,R}(e)\).
The accepted scalar bounds
\[
 \lambda(e)<433/500\quad(e<1/2),\qquad
 \max(-J)<1/6,\qquad
 \max(\lambda+J)<101/125
                                                               \tag{9}
\]
therefore retain the ceiling \(B_0=1549/1500\).
The endpoint rate in (6) is strictly smaller. After one arbitrary
total finite-product tolerance, the entire original first cap has
\[
 \sup_{w\in[-2,2]}|U_{0,N}(w,e^{-2\pi i(x+ih)})|
 \le C_\tau N^{B_\tau}e^{N(B_0+\tau)},
 \quad B_0=1549/1500,\quad 1/2\le x\le1,\quad c\le h\le0.
                                                               \tag{10}
\]
All physical rows, including those that revive at nonsampled incoming
points, have been included. The proof has used no off-grid endpoint
claim for \(H_N\).

## 3. Every physical terminal row retains its original all-color bound

For a physical transform index \(i<N\), the exact source is
\[
 U_{1,N}(w,r^i)
   =\sum_{j=0}^{N-1-i}
        \frac{H_N(w,r^{-j})}{P_j}
                         \frac{P_{i+j}}{P_iP_j}.
                                                               \tag{11}
\]
The positive sum of complete coefficient moduli obeys
\[
 \sup_{w\in[-2,2]}
       \sum_{j=0}^{N-1}\frac{|H_N(w,r^{-j})|}{S_j}
       \le C_\tau N^{B_\tau}e^{N(b_1+\tau)},
                       \qquad b_1=433/500.
                                                               \tag{12}
\]
This is Lemma 2 of terminal real-color decay. Its proof uses (3)
only on compact physical indices and the original exact endpoint
estimates at both ends; its upper Newton rows use
\(V_\theta(u)\le0\), not the smaller complete-color entropy.

Let \(t=i/N\) and \(L(t)=-2J((1-t)/2)\). On the exact
support \(0\le e=j/N\le1-t\), the quotient rate has maximum
\[
 \max_e\{J(t+e)-J(t)-J(e)\}=L(t)-J(t).
                                                               \tag{13}
\]
The uniform factorial bounds apply even at the two support ends.
Equations (11)--(13) prove, for all physical \(i<N\),
\[
 \sup_{w\in[-2,2]}|U_{1,N}(w,r^i)|
 \le C_\tau N^{B_\tau}
                 e^{N\{b_1+L(t)-J(t)+\tau\}}.
                                                               \tag{14}
\]
This retains the complete cap at \(i=0\) and \(i=N-1\).
Its private and Newton sums are not replaced by isolated leading
terms. Only the bound for the whole finite coefficient in (12)
is multiplied by a positive quotient bound.

## 4. The complete complementary source, including ordinary derivatives

The only color-dependent inputs in complementary-contour completion
were (10) and (14). Every subsequent product and scalar comparison
is color independent. For reference, its literal terminal row rate,
including \(X^{-i}\), is
\[
 b_1+L(t)-3J(t)+I_{x,e^{2\pi h}}(t)-2\pi ht.
                                                               \tag{15}
\]
On the real far half, its lower transform part combines with (10)
to give ceiling \(3979/1500\), and its upper part gives
\(1643/750\). On the vertical connector, put
\(\delta=-2\pi h<11/50\). The exact radius identity and
monotonicity above \(t=1/3\) give the lower-transform ceiling
\[
 \frac{3979}{1500}+\frac{11}{300}+\frac7{1920}
       =\frac{27}{10}-\frac{337}{48000}<M-\frac1{150}.
                                                               \tag{16}
\]
The remaining upper-transform rows have ceiling \(613/250\).
These are precisely the already reviewed inequalities of that
theorem; no new source or phase value is substituted. Allocate the
total tolerances in (10), (14) and the numerator estimate below
\(1/300\).

**Theorem 1.** For every fixed pair of ordinary derivative orders
\(k,\ell\), both level parities satisfy
\[
 \begin{split}
 &|\partial_{w_L}^{k}U_{0,N}(w_L,X)|
   \sum_{i=0}^{N-1}
      \left|\frac{X^{-i}p_i(X)}{P_i^2}\right|
                    |\partial_{w_R}^{\ell}U_{1,N}(w_R,r^i)|\\
 &\hspace{12mm}\le C_{k,\ell}N^{B_{k,\ell}}
                                e^{N(M-1/300)},
 \quad X=e^{-2\pi ia},\quad a\in\Gamma_+,\quad
                       w_L,w_R\in[-2,2].
 \end{split}                                                    \tag{17}
\]

For the derivative assertion, \(U_0(w,X)\) and each whole
\(U_1(w,r^i)\) are polynomials of ordinary degree at most
\(N-1\). Apply the real-interval Markov inequality to (10)
and (14) separately before taking the product and summing (17).
The latter bound retains its own \(i\)-dependent exponent under
the supremum over real \(w\). A fixed derivative costs at most
\(C_kN^{2k}\). The same inequality holds for complex polynomial
coefficients: rotate the derivative value at the point in question
and apply the real inequality to the real part of the rotated
polynomial. Thus no complex-color packet at a distant color, or
division by a vanishing finite source, is used.

## 5. Explicit losses at both ordinary endpoints

Write \(w_L=-2\cos\theta_L\), \(w_R=-2\cos\theta_R\),
and \(D(\theta)=1-\cos\theta\). Since each \(D\in[0,2]\),
\[
 \frac1{600}+\frac{D(\theta_L)+D(\theta_R)}{2400}
                              \le\frac1{300}.
                                                               \tag{18}
\]
Consequently (17), with every fixed ordinary derivative, implies
the explicit pointwise bound
\[
 \begin{split}
 &|\partial_{w_L}^{k}U_{0,N}(-2\cos\theta_L,X)|
   \sum_{i=0}^{N-1}
      \left|\frac{X^{-i}p_i(X)}{P_i^2}\right|
        |\partial_{w_R}^{\ell}U_{1,N}(-2\cos\theta_R,r^i)|\\
 &\quad\le C_{k,\ell}N^{B_{k,\ell}}
   \exp N\left\{M-\frac1{600}
          -\frac{D(\theta_L)+D(\theta_R)}{2400}\right\},
                  \qquad a\in\Gamma_+.
 \end{split}                                                    \tag{19}
\]
These angular losses spend part of an already proved uniform
source-region gap. They do not assert that every individual end row
strictly decreases with angle, or that the signed source is largest
at complete color.

In particular define the complete original complementary observation
\[
 I_{+,N}(w_L,w_R)=\kappa_N^3N^2\int_{\Gamma_+}
                 U_{0,N}(w_L,e^{-2\pi ia})
                 V_{1,N}(w_R,e^{-2\pi ia})\,da.
                                                               \tag{20}
\]
Bounded contour length, the exact \(N^2\), and (19) give
\[
 |\partial_{w_L}^k\partial_{w_R}^{\ell}
                I_{+,N}(-2\cos\theta_L,-2\cos\theta_R)|
 \le C_{k,\ell}N^{B_{k,\ell}}
   e^{N\{M-1/600-[D(\theta_L)+D(\theta_R)]/2400\}}.
                                                               \tag{21}
\]
The product is entire and one-periodic in the incoming coordinate,
so this is the same complementary integral with the original fixed
endpoints, for every real pair of ordinary colors and their fixed
normals. No sampled root sector is identified with an arc.

The present result supplies the full-real-color estimate for this
complete complementary part. The first-half source must still be
combined with its own full-real-color bounds to obtain a whole
outside-color theorem. No new far-color saddle, general short-cluster
stability, or knot-family conclusion is inferred from (21) alone.
