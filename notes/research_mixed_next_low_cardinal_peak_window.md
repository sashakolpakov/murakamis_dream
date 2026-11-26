# The actual cumulative row through the Fourier-profile maximum

Research deduction, 7 November 2026. The initialized first-node
cumulative response has the same nonzero endpoint symbol throughout
every fixed two-sided square-root window around the maximum of the
original Fourier column. The proof uses the exact forced increment
and a nonresonant telescoping coefficient. It does not require
absolute geometric contraction at the maximum or a differentiable
error in the column asymptotic.

The result also gives explicit smoothly windowed Fourier observations.
Keeping the absolute accumulated error and the original global column
tails gives the norm and Gaussian Fourier-band mass of the full
cumulative vector. No claim about the complete outgoing Newton
evaluation or a pointwise relative packet on a fixed interval beyond
the maximum is made. No numerical evaluation is used.

## 1. Original source and a nonresonant exact telescoper

Keep the exact definitions, normalizations and branches of
[the cumulative endpoint packet](research_mixed_next_low_cardinal_endpoint_packet.md).
In particular, at both level parities,
\[
 \begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{D^2/2},\quad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\\
 \gamma=MJM^3e_0,\qquad v_j=(-q)^{-j}\gamma_j,\\
 a_0=1-\frac{\gamma_0}{\kappa^2N^2},\qquad
 a_j-a_{j-1}=-\frac{1}{\kappa^2N^2}
       \left(v_j+\frac{r^j}{1-r^j}v_{j-1}\right).
 \end{gathered}
 \tag{1}
\]
These are the full moment coefficients of the two original first-node
Fourier sectors. Their outgoing rows are respectively
\(a_jp_j(Z)/P_j^{1+\beta}\) and
\((1-a_j)p_j(Z)/P_j^{1+\beta}\), with \(P_j=(r;r)_j\).
No endpoint or forcing term in (1) is replaced.

For \(0<t<1/2\), write
\[
 \begin{gathered}
 X=e^{-2\pi it},\quad d(t)=4\sin^2\pi t,\quad
 \lambda=\frac{3-2X+\sqrt{4/X-3}}2,\quad
 \mu=\frac{3-2X-\sqrt{4/X-3}}2,\\
 I(t)=\int_0^t\log\lambda(s)\,ds,\qquad
 J(t)=\int_0^t\log(2\sin\pi s)\,ds,\qquad
 A(t)=\Re I(t)-2J(t),\\
 G(t)=\sqrt{\frac{\lambda(t)}{\lambda(t)-\mu(t)}},\qquad
 \rho(t)=\frac{d(t)}{\lambda(t)},\qquad
 u(t)=\frac{1-\sqrt{4/X(t)-3}}2 .
 \end{gathered}
 \tag{2}
\]
The original square root, logarithm and \(G\) continue from
\(+1,0,1\) at zero. The
[original Fourier-column theorem, equations (4)--(9) and Lemma 1](research_three_crossing_next_crossing_fourier.md)
proves, for each fixed \(b<1/2\),
\[
 v_j=\gamma_0 S_j^{-2}G(j/N)e^{NI(j/N)}
                    (1+O_b(N^{-1})),\qquad 0\le j\le bN,
 \quad |\gamma_0|=N^{3/2}(1+O(N^{-1})).
 \tag{3}
\]
It also proves that \(A\) has a unique nondegenerate maximum
\(x_*\in(1/3,1/2)\), with \(A'>0\) before that maximum.
Put \(\alpha=-A''(x_*)>0\).

The exact root identities established in the endpoint note give
\[
 B(t)=1-\frac{1-X(t)}{\lambda(t)},\qquad
 F(t)=\frac{B(t)}{1-\rho(t)}
      =\frac{\lambda(t)-1+X(t)}{\lambda(t)-d(t)}
      =\frac1{1-u(t)}.
 \tag{4}
\]
In particular \(\lambda-d=(1-u)^2\ne0\) throughout
\((0,1/2)\). Thus \(F\) is smooth and nonzero on a fixed
neighborhood of \(x_*\), although \(|\rho(x_*)|=1\).
This is the nonresonance needed below.

Fix \(a\in(0,x_*)\), \(0\le T<\infty\), and a fixed
\(b\in(x_*,1/2)\). Let \(k_0=\lfloor aN/2\rfloor\) and
\(t_k=k/N\). For all sufficiently large \(N\), the compact
interval containing \(t_{k_0-1},\ldots,b\) lies in \((0,1/2)\).
Equation (3), divided at consecutive indices, implies
\[
       R_k:=\frac{v_{k-1}}{v_k}
                     =\rho(t_k)+O(N^{-1})
                  \qquad(k_0\le k\le bN).
 \tag{5}
\]
The error in this statement need not have any smoothness in \(k\).

Define an exact residual and an exact initial constant by
\[
 \begin{split}
 \varepsilon_{k,N}
  &=v_k+\frac{r^k}{1-r^k}v_{k-1}
       -\{F(t_k)v_k-F(t_{k-1})v_{k-1}\},\\
 H_N&=\kappa^2N^2a_{k_0-1}+F(t_{k_0-1})v_{k_0-1}.
 \end{split}
 \tag{6}
\]
Writing \(c(t)=X(t)/(1-X(t))\), the identity
\(1+c(t)\rho(t)=B(t)=F(t)(1-\rho(t))\), together with
(5) and \(F(t_k)-F(t_{k-1})=O(N^{-1})\), gives
\[
                         |\varepsilon_{k,N}|
                               \le C N^{-1}|v_k|.
 \tag{7}
\]
Summing (1) now yields the exact source formula
\[
 \boxed{\quad
 \kappa^2N^2a_j=-F(t_j)v_j+H_N
                         -\sum_{k=k_0}^{j}\varepsilon_{k,N}.
 \quad}
 \tag{8}
\]
The actual initialization survives in \(H_N\); it has not been
set to zero or chosen to remove a complementary solution.

## 2. Gaussian control of the entire backward sum

On each compact subinterval of \((0,1/2)\), (3) and the original
uniform sine-factorial expansion give
\[
             cN^{1/2}e^{NA(t_k)}
                       \le |v_k|\le CN^{1/2}e^{NA(t_k)}.
 \tag{9}
\]
By nondegeneracy and strict increase before \(x_*\), there is
\(c_0>0\) such that
\[
                    A'(s)\ge c_0(x_*-s)
                  \qquad(a/3\le s\le x_*).
 \tag{10}
\]
Indeed the quotient extends to the positive value
\(-A''(x_*)\) at its right endpoint and is positive on the
remaining compact interval.

If \(t_k\le t_j\le x_*\), integration of (10) gives
\[
 A(t_j)-A(t_k)
 \ge c_0\{(x_*-t_j)(t_j-t_k)+(t_j-t_k)^2/2\}
 \ge c_0(t_j-t_k)^2/2 .
 \tag{11}
\]
The Gaussian lattice sum and (9) therefore imply
\[
              \sum_{k=k_0}^{j}|v_k|
                              \le C\sqrt N\,|v_j|
                      \qquad(a\le t_j\le x_*).
 \tag{12}
\]
For \(x_*\le t_j\le x_*+T/\sqrt N\), Taylor's theorem instead
gives \(A(t_j)\ge A(x_*)-C_T/N\). For \(t_k\le x_*\),
(10) bounds the loss from \(A(x_*)\) quadratically; the remaining
at most \(T\sqrt N+1\) terms have modulus at most a fixed
multiple of \(|v_j|\). Hence
\[
 \boxed{\quad
   \sum_{k=k_0}^{j}|v_k|
       \le C_T\sqrt N\,|v_j|,
       \qquad a\le j/N\le x_*+T/\sqrt N .
 \quad}
 \tag{13}
\]
The Gaussian-sum estimate is a comparison with its convergent
integral, not an evaluation of the original action or source.

The indices before \(k_0\) are estimated before any division by
\(v_j\). The endpoint-uniform formula (3), the uniform
sine-factorial estimate, and increase of \(A\) show that their
total contribution to \(H_N\) is bounded by
\[
            |H_N|\le CN^C
                 \exp\{N A(a/2+1/N)\}.
 \tag{14}
\]
Here \(|1-r^k|^{-1}\le N/4\) controls every nonzero small
denominator in (1), and its actual \(a_0\) contributes only
polynomial size. Since \(A(a)>A(a/2)\), equations (9) and
(14) imply, uniformly in the range of (13),
\[
                              |H_N/v_j|\le Ce^{-cN}.
 \tag{15}
\]
The rightmost \(T/\sqrt N\) extension has action tending to
\(A(x_*)>A(a)\), so it does not alter this strict early-source gap.

**Theorem 1.** Uniformly for physical indices
\[
                       a\le j/N\le x_*+T/\sqrt N
 \tag{16}
\]
and both parities,
\[
 \boxed{\quad
 a_j=-\frac{v_j}{\kappa^2N^2(1-u(j/N))}
                  \bigl(1+O_{a,T}(N^{-1/2})\bigr).
 \quad}
 \tag{17}
\]
In particular the complete initialized row is nonzero throughout
this range for all sufficiently large levels.

*Proof.* Substitute (7), (13), and (15) into the exact identity
(8), and use that \(F\) is bounded away from zero on the fixed
compact interval. This gives (17). No pointwise smoothness
assumption on the error in (3) is used. \(\square\)

Using the endpoint note's exact action and scalar calibration,
\[
 \mathcal H(t)=I(t)-2J(t)-i\pi/12,\qquad
 \frac{\gamma_0}{\kappa^2}
 =N^{3/2}\exp i\pi(1/4+1/(4N)-N/12)(1+O(N^{-1})),
 \tag{18}
\]
equation (17) becomes
\[
 a_j=-e^{i\pi/4}N^{-3/2}
       \frac{G(t_j)}{2\sin(\pi t_j)(1-u(t_j))}
       e^{N\mathcal H(t_j)}
                    \bigl(1+O_{a,T}(N^{-1/2})\bigr).
 \tag{19}
\]
On output compacts where \(z\), \(t+z\) remain in the original
regular strips, multiplication by the original factorial packet
extends the endpoint note's entire outgoing row formula (31)
to (16), with the same nonzero symbol and
\(O(N^{-1/2})\) relative error. Fixed outgoing derivatives follow
by Cauchy on smaller compacts. No incoming derivative of the
discrete sequence is inferred.

## 3. Explicit windowed observations of the actual coefficients

Choose a fixed nonnegative, nonzero \(C^2\) function
\(\chi\) of compact support on \(\mathbb R\). Put
\[
 s_j=\frac{j-Nx_*}{\sqrt N},\qquad
 h(s)=\chi(s)e^{-\alpha s^2/2},\qquad
 H_*=\frac{|F(x_*)G(x_*)|}{2\sin(\pi x_*)}>0 .
 \tag{20}
\]
For indices in this window define the unit phase
\[
 \sigma_{N,j}
 =-\frac{\gamma_0}{\kappa^2|\gamma_0|}
      \frac{F(t_j)G(t_j)}{|F(t_j)G(t_j)|}
                        e^{iN\Im I(t_j)} .
 \tag{21}
\]
Outside a fixed compact neighborhood of \(x_*\), define it
arbitrarily with unit modulus; \(\chi(s_j)=0\) there for large \(N\).
The actual windowed vector and its normalization are
\[
      w_{N,j}=\chi(s_j)\sigma_{N,j}^{-1}a_j,\qquad
                    z_N=w_N/\|w_N\|_2 .
 \tag{22}
\]
The window is an explicitly stated linear observation; it is not
asserted that the unwindowed complementary indices are negligible.

**Theorem 2.** These actual vectors satisfy
\[
 \begin{split}
 \|w_N\|_2
   &=H_*N^{-5/4}e^{NA(x_*)}\|h\|_{L^2(\mathbb R)}
                           (1+O(N^{-1/2})),\\
 \widehat z_N(m)
   &=N^{-1/4}e^{-2\pi imx_*}
       \frac{\displaystyle\int_{\mathbb R}
                  h(s)e^{-2\pi i(m/\sqrt N)s}\,ds}
            {\|h\|_{L^2(\mathbb R)}}+O_T(N^{-3/4}),
              \qquad |m|\le T\sqrt N,\\
 \|\mathsf Sz_N-z_N\|_2&=O(N^{-1/2}),
       \qquad(\mathsf Sz)_j=z_{j-1\bmod N}.
 \end{split}
 \tag{23}
\]
The Fourier transform is
\(\widehat z_N(m)=N^{-1/2}\sum_{j=0}^{N-1}z_{N,j}e^{-2\pi imj/N}\).
In particular \(|\widehat z_N(0)|\ge cN^{-1/4}\).

*Proof.* On the fixed support of \(\chi(s_j)\), (3), (17), and
the uniform compact sine-factorial expansion yield
\[
 w_{N,j}=H_*N^{-3/2}e^{NA(x_*)}
           \{h(s_j)+O(N^{-1/2})\chi(s_j)\}.
 \tag{24}
\]
The error is uniform there. Taylor expansion at the actual
nondegenerate maximum supplies
\(N(A(t_j)-A(x_*))=-\alpha s_j^2/2+O(N^{-1/2})\);
the smooth prefactor has the same order of variation.
Riemann sums of mesh \(N^{-1/2}\), uniform in the offset of
\(Nx_*\) from the lattice, now give the norm and Fourier formulas
in (23). Their error is uniform for \(m/\sqrt N\) in a compact
interval. The relative vector error after normalization is
\(O(N^{-1/2})\) in \(\ell^2\).

For the positive model \(h(s_j)/(\sum_kh(s_k)^2)^{1/2}\), its
adjacent difference has norm \(O(N^{-1/2})\), by the bounded
derivative and compact support of \(h\). The actual normalized
vector differs from that model by \(O(N^{-1/2})\) in norm, so
the same upper bound follows by the triangle inequality. The
support stays a fixed distance from the cyclic seam. Finally
\(\int h>0\) gives the nonzero Fourier conclusion. \(\square\)

## 4. The full cumulative vector and its Fourier-band mass

The original global column estimate also controls what the local
relative statement does not. Fix \(0<a<x_*<b<1/2\), and set
\[
 p_{N,j}=
 \begin{cases}
 -F(t_j)v_j/(\kappa^2N^2),&a\le t_j\le b,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{25}
\]
This comparison vector uses the actual column \(v\), including its
original normalization. Let \(\mathbf a_N=(a_j)_{j=0}^{N-1}\).

**Theorem 3.** The complete initialized vector satisfies
\[
 \begin{split}
 \|\mathbf a_N-p_N\|_2
       &=O(N^{-3/2}e^{NA(x_*)}),\\
 \|\mathbf a_N\|_2
       &=H_*\left(\frac{\pi}{\alpha}\right)^{1/4}
           N^{-5/4}e^{NA(x_*)}(1+O(N^{-1/4})).
 \end{split}
 \tag{26}
\]
Use the phase (21) for \(a\le t_j\le b\), and any unit phase
elsewhere. Define the whole normalized vector
\[
               \zeta_{N,j}
                 =\sigma_{N,j}^{-1}a_j/\|\mathbf a_N\|_2 .
 \tag{27}
\]
For every fixed \(T>0\), its actual Fourier transform satisfies
\[
 \begin{split}
 \sum_{|m|\le T\sqrt N}|\widehat\zeta_N(m)|^2
   &=\left(\frac{4\pi}{\alpha}\right)^{1/2}
       \int_{-T}^{T}e^{-4\pi^2s^2/\alpha}\,ds
                                  +O_T(N^{-1/4}),\\
 \|\mathsf S\zeta_N-\zeta_N\|_2&=O(N^{-1/4}).
 \end{split}
 \tag{28}
\]
In particular some integer \(m_N\) with
\(|m_N|\le T\sqrt N\) has
\(|\widehat\zeta_N(m_N)|\ge c_TN^{-1/4}\).
The theorem does not specify that mode as \(m_N=0\).

*Proof.* On the fixed interval \([a/3,b]\), the original
nondegenerate profile and its unique maximum imply
\[
                        \sum_{k=k_0}^{\lfloor bN\rfloor}|v_k|
                                      \le CN e^{NA(x_*)}.
 \tag{29}
\]
Indeed (9) has prefactor \(N^{1/2}\), the peak has a
\(\sqrt N\)-sized lattice window, and its fixed complement
has a strict exponential gap. Equations (7)--(8), together
with the early bound (14), give the uniform absolute estimate
\[
 \left|a_j+\frac{F(t_j)v_j}{\kappa^2N^2}\right|
                 \le CN^{-2}e^{NA(x_*)},
                       \qquad a\le t_j\le b .
 \tag{30}
\]
This does not divide by \(v_j\) to the right of the maximum.

Lemma 2 of the original Fourier-column theorem supplies a
strict global gap for \(|\gamma_j|=|v_j|\) outside any fixed
neighborhood of \(x_*\). Choose that neighborhood with closure
in \((a,b)\). Summing the exact increments (1) over \(j<aN\)
therefore bounds every early \(a_j\) by
\(CN^C e^{N(A(x_*)-\eta)}\), for some \(\eta>0\), including
the polynomial initial value. At \(j_b=\lfloor bN\rfloor\),
the particular term has the same kind of strict gap.
Equation (30) consequently gives
\[
                          |a_{j_b}|
                               \le CN^{-2}e^{NA(x_*)}.
 \tag{31}
\]
For every later index, sum (1) starting at \(j_b\). All of
the later \(v_k\) and \(v_{k-1}\) have the original global gap.
The uniform bound \(|1-r^k|^{-1}\le N/4\), including the
last nonzero index, and the \(N\) possible increments incur
only polynomial cost. Hence (31) remains valid for every
\(j>j_b\). This retains the possible cumulative homogeneous
plateau; it bounds it absolutely rather than declaring it zero.
Taking the norm of these three regions proves the first line
of (26).

The norm of the particular vector follows from the original
compact factorial packet and a Gaussian sum:
\[
 \|p_N\|_2
     =H_*\left(\frac{\pi}{\alpha}\right)^{1/4}
       N^{-5/4}e^{NA(x_*)}(1+O(N^{-1/2})).
 \tag{32}
\]
Thus the first line of (26) is a relative \(O(N^{-1/4})\)
error, and proves its second line.

For completeness, the positive model on \(a\le t_j\le b\) is
\[
 h_{N,j}=\frac{|\gamma_0|}{N^2S_j^2}
                |F(t_j)G(t_j)|e^{N\Re I(t_j)},
 \tag{33}
\]
extended by zero and normalized to a vector \(h_N^\circ\).
Equations (3), (26), and (32) imply
\[
                         \|\zeta_N-h_N^\circ\|_2
                                          =O(N^{-1/4}).
 \tag{34}
\]
The smooth, nonzero multiplier \(|F|\) leaves the normalized
leading Gaussian of the original Fourier theorem unchanged.
Its same Gaussian Riemann-sum proof gives, uniformly for
\(|m|\le T\sqrt N\),
\[
 \widehat h_N^\circ(m)
 =\left(\frac{4\pi}{\alpha}\right)^{1/4}
       N^{-1/4}e^{-2\pi imx_*}
         e^{-2\pi^2m^2/(\alpha N)}(1+O_T(N^{-1/2})),
 \quad
 \|\mathsf Sh_N^\circ-h_N^\circ\|_2=O(N^{-1/2}).
 \tag{35}
\]
The truncation boundaries have a strict profile gap and do
not change either estimate. Plancherel and (34) transfer the
band norm with an \(O(N^{-1/4})\) error; summing the Gaussian
squares in (35) proves (28). The shift bound follows from
(34) and the triangle inequality. The limiting band mass is
positive, and the band has \(O_T(\sqrt N)\) indices, proving
the existence of the displayed mode. \(\square\)

The complementary coefficient vector \((1-a_j)_j\) has the
same conclusions with the opposite phase: its difference from
\(-\mathbf a_N\) is the constant vector of norm \(\sqrt N\),
exponentially smaller than (26). This statement preserves their
exact coefficientwise cancellation; it does not estimate either
complete outgoing sector.

## 5. Scope of the extension

The window in (16) reaches a fixed number of Gaussian widths
past the maximum. This follows from (13), not from an absolute
ratio smaller than one there. The exact homogeneous term and
residual in (8) remain present.

For a fixed interval beyond \(x_*\), the denominator \(1-u\)
still exists, but the quotient of the accumulated residual by
\(v_j\) need no longer be small. Theorem 3 uses its absolute
size and the actual global column tail, not a relative packet
or an exponentially small homogeneous coefficient there.

The explicit window in Theorem 2 is essential to its prescribed
zero-mode conclusion. The full-vector error in (34) is of the
same order as a single leading Fourier coefficient, so Theorem 3
only asserts band mass and existence of some mode.
These Fourier transforms act on the index \(j\); they are not
the original outgoing Newton evaluation
\(\sum_j a_jp_j(Z)/P_j^{1+\beta}\). No lower or upper bound
for that complete evaluation, an ordinary boundary observation,
or either whole outgoing sector follows from the present theorem.
