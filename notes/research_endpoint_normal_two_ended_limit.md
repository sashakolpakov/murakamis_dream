# The two-ended limit of the original microscopic endpoint normal

Private written proof, 16 November 2026.

The first normal at the original physical endpoint has a limit after
division by \(N^2\). Both ends of its Newton sum contribute. A uniform
inverse-square bound controls the intervening indices and justifies
the limit on every bounded complex parameter disk, including the
apparent zeros of the complementary formula. The resulting function
is entire and strictly positive on the real parameter axis.

This is the original endpoint normal constant. It is not either of
the two bulk scalar-compatibility coefficients, and does not determine
their cancellation with the coefficient-shift channel.

## 1. Exact endpoint normal and complementary identity

Use
\[
 N\ge2,\quad D=N-1,\quad \theta=\pi/N,\quad \eta=(-1)^D,\qquad
 s_r=2\sin(r\theta),\quad S_i=\prod_{r=1}^i s_r,\quad S_0=1,
\]
\[
 c_r=2\cos((2r+1)\theta),\quad
 e_i(Z)=S_i^{-2}\prod_{r=0}^{i-1}(c_r-Z),\quad
 K_N(Z,w)=\sum_{i=0}^{D}e_i(Z)e_i(w),
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 w_N(\alpha)=2\cosh(\alpha/N),\qquad
 Q_N(\alpha)=
      \left.\partial_ZK_N(Z,w_N(\alpha))\right|_{Z=c_0}.
 \tag{1}
\]
The polynomials and derivative are the ordinary original ones, before
any quotient or free-boundary replacement.

For \(1\le i<N\), the difference-of-cosines identity gives
\[
 c_r-c_0=-s_rs_{r+1}\quad(1\le r<N-1),\qquad
                         e_i'(c_0)=\frac{(-1)^i}{s_1s_i}.
 \tag{2}
\]
Indeed only the factor \(c_0-Z\) is differentiated, and the remaining
product is
\((-1)^{i-1}S_{i-1}S_i/s_1\). Thus exactly
\[
 \boxed{\quad
 \frac{Q_N(\alpha)}{N^2}
     =\sum_{i=1}^{N-1}q_{i,N}(\alpha),\qquad
 q_{i,N}(\alpha)=
          \frac{(-1)^i e_i(w_N(\alpha))}{N^2s_1s_i}.
 \quad}
 \tag{3}
\]
For real \(\alpha\), every summand is strictly positive.

Put \(E_{i,N}(\alpha)=(-1)^i e_i(w_N(\alpha))\). The full physical
polynomial and the sine product give
\[
 S_{N-1}=N,\qquad
 P_N(w_N(\alpha))=4\cosh^2(\alpha/2),
\]
\[
 \boxed{\quad
 E_{N-m,N}(\alpha)
       =\frac{P_N(w_N(\alpha))}
                        {N^2s_m^2 E_{m,N}(\alpha)}
                      \qquad(1\le m<N).
 \quad}
 \tag{4}
\]
At a zero of a denominator, (4) means its removable entire continuation.
To verify it, the last \(m\) roots in the full product for \(P_N\)
are \(c_0,\ldots,c_{m-1}\) in reverse order and
\(S_{N-m}=N/S_{m-1}\). Therefore
\[
 E_{N-m,N}
  =\frac{P_N(w_N)S_{m-1}^2}
             {N^2\prod_{r<m}(w_N-c_r)}
  =\frac{P_N(w_N)}{N^2s_m^2E_{m,N}}.
\]
This is an identity of ordinary functions, not an omitted high sector.

## 2. Uniform inverse-square tails at both ends

Let \(d_i=\min(i,N-i)\). For each fixed \(A<\infty\), there is \(C_A\)
such that
\[
 \boxed{\qquad
 |q_{i,N}(\alpha)|\le \frac{C_A}{d_i^2}
       \quad(1\le i<N,\ |\alpha|\le A,\ N\ge2).
 \qquad}
 \tag{5}
\]

Here is a proof uniform through the middle of the original list.
At \(\alpha=0\), set \(a_{i,N}=E_{i,N}(0)=|e_i(2)|\). Directly
\[
 a_{i,N}
  =\prod_{r=0}^{i-1}
      \left(\frac{\sin((r+1/2)\theta)}
                       {\sin((r+1)\theta)}\right)^2.
 \tag{6}
\]
For \(1\le i\le N/2\), split the sine into its argument and
\(f(v)=\sin v/v\), with \(f(0)=1\). This function decreases on
\([0,\pi/2]\), so
\[
 1\le
 \prod_{r<i}\frac{f((r+1/2)\theta)}{f((r+1)\theta)}
 \le \frac1{f(i\theta)}\le\frac{\pi}{2}.
 \tag{7}
\]
For the middle inequality, the logarithm is the integral of
\(-(\log f)'\) over disjoint half-step subintervals of \([0,i\theta]\).
The remaining rational product is \((1/2)_i/i!\). The elementary
central-binomial bounds therefore give absolute constants \(c,C>0\)
such that
\[
 \frac{c}{i+1}\le
 \left(\frac{(1/2)_i}{i!}\right)^2
 \le a_{i,N}\le
 \frac{\pi^2}{4}\left(\frac{(1/2)_i}{i!}\right)^2
 \le\frac{C}{i+1}.
 \tag{8}
\]
Equation (4) at \(\alpha=0\) gives
\[
                   a_{N-m,N}=\frac4{N^2s_m^2a_{m,N}}.
 \tag{9}
\]
For \(m\le N/2\),
\(4m/N\le s_m\le2\pi m/N\). Equations (8)--(9) show
\[
                         a_{i,N}\le C/d_i
                         \quad(1\le i<N).
 \tag{10}
\]

The same bound controls every bounded complex parameter disk.
The power series for cosh gives
\[
 |w_N(\alpha)-2|
       \le2\cosh(A/N)-2\qquad(|\alpha|\le A).
 \tag{11}
\]
Each \(2-c_r\) is positive. Hence
\[
 \frac{|e_i(w_N(\alpha))|}{|e_i(2)|}
 \le\prod_{r<i}
       \left(1+\frac{2\cosh(A/N)-2}{2-c_r}\right)
 \le\prod_{r=0}^{N-1}
       \frac{2\cosh(A/N)-c_r}{2-c_r}
 =\cosh^2(A/2).
 \tag{12}
\]
The last equality uses the literal \(P_N\), with all repeated roots
and the odd simple root included. Finally \(s_1\ge4/N\) and
\(s_i=s_{d_i}\ge4d_i/N\). Substitution of (10)--(12) in (3) proves
(5).

In particular, for every integer \(L\ge1\) with \(2L<N\),
\[
 \sup_{|\alpha|\le A}
 \sum_{L<i<N-L}|q_{i,N}(\alpha)|\le C_A/L.
 \tag{13}
\]
This is the uniform middle-tail control needed before passing
either end to a limiting series.

## 3. The limiting entire function

Define the entire polynomials
\[
 \mathsf E_m(\alpha)
   =\frac{(1/2+i\alpha/(2\pi))_m
           (1/2-i\alpha/(2\pi))_m}{(m!)^2}
   =\prod_{r=0}^{m-1}
       \frac{(r+1/2)^2+(\alpha/(2\pi))^2}{(r+1)^2}.
 \tag{14}
\]
For fixed positive \(i\), the ordinary sine products in (1) give
locally uniformly in \(\alpha\)
\[
 E_{i,N}(\alpha)\longrightarrow\mathsf E_i(\alpha),\qquad
 q_{i,N}(\alpha)\longrightarrow
             \mathsf L_i(\alpha):=\frac{\mathsf E_i(\alpha)}{4\pi^2i}.
 \tag{15}
\]
For the other end, (4) gives, for fixed positive \(m\),
\[
 q_{N-m,N}(\alpha)\longrightarrow
 \mathsf H_m(\alpha):=
       \frac{\cosh^2(\alpha/2)}
                           {4\pi^4m^3\mathsf E_m(\alpha)}.
 \tag{16}
\]
The apparent poles in \(\mathsf H_m\) are removable. Every zero
of \(\mathsf E_m\) is a simple zero among
\(\alpha=\pm i(2r+1)\pi\), \(0\le r<m\), whereas
\(\cosh^2(\alpha/2)\) has a double zero there. Thus
\(\mathsf H_m\) denotes an entire function.

The locally uniform limit in (16), including those zeros, also follows
directly from the exact unit factorization in the next section.
Passing the uniform finite bound (5) to each fixed end yields
\[
 \sup_{|\alpha|\le A}
       (|\mathsf L_m(\alpha)|+|\mathsf H_m(\alpha)|)
                                      \le C_A/m^2.
 \tag{17}
\]
Consequently the function
\[
 \boxed{\quad
 \mathcal Q(\alpha)=
 \frac1{4\pi^2}\sum_{i=1}^{\infty}\frac{\mathsf E_i(\alpha)}{i}
 +\frac{\cosh^2(\alpha/2)}{4\pi^4}
       \sum_{m=1}^{\infty}\frac1{m^3\mathsf E_m(\alpha)}
 \quad}
 \tag{18}
\]
is interpreted by the entire summands in (16), and both sums converge
normally on every bounded complex disk. It is an even entire function.
For real \(\alpha\), all summands in both series are strictly positive,
so
\[
                             \mathcal Q(\alpha)>0.
 \tag{19}
\]

**Theorem.** Uniformly on every bounded complex parameter disk,
\[
              \frac{Q_N(\alpha)}{N^2}\longrightarrow\mathcal Q(\alpha).
 \tag{20}
\]
Every fixed parameter derivative converges uniformly on smaller disks.
In fact the quantitative estimate
\[
 \sup_{|\alpha|\le A}
 \left|\frac{Q_N(\alpha)}{N^2}-\mathcal Q(\alpha)\right|
                                  \le C_A N^{-1/2}
 \tag{21}
\]
holds for all sufficiently large \(N\). The same rate holds for each
fixed \(\alpha\)-derivative, after using a larger fixed parameter disk.

Even without the quantitative argument, (20) follows by retaining
the first \(L\) terms at each end, using (15)--(16), and then using
(13),(17) before sending \(L\) to infinity. No unbounded Newton
range is replaced by its fixed-index limit without this tail control.

## 4. Quantitative comparison through the apparent zeros

Write \(\operatorname{sinhc}z=\sinh z/z\) and
\(\operatorname{sinc}z=\sin z/z\), with their removable values one.
There is an exact entire factorization
\[
 w_N(\alpha)-c_r
 =\frac{\alpha^2+(2r+1)^2\pi^2}{N^2}
   \operatorname{sinhc}\!\left(\frac{\alpha+i(2r+1)\pi}{2N}\right)
   \operatorname{sinhc}\!\left(\frac{\alpha-i(2r+1)\pi}{2N}\right).
 \tag{22}
\]
It is the identity
\(2\cosh u-2\cos v
 =4\sinh((u+iv)/2)\sinh((u-iv)/2)\).
Dividing the exact finite product by its sine denominators gives
\[
 E_{i,N}(\alpha)=\mathsf E_i(\alpha)\,\mathsf U_{i,N}(\alpha),
\]
\[
 \mathsf U_{i,N}(\alpha)=
 \prod_{r=0}^{i-1}
 \frac{
 \operatorname{sinhc}((\alpha+i(2r+1)\pi)/(2N))
 \operatorname{sinhc}((\alpha-i(2r+1)\pi)/(2N))}
 {\operatorname{sinc}(\pi(r+1)/N)^2}.
 \tag{23}
\]
This identity holds at zeros of \(\mathsf E_i\); it is not obtained
by dividing pointwise there.

Let \(L=\lfloor\sqrt N\rfloor\). For \(|\alpha|\le A\) and \(i\le L\),
all factors in (23) are units in one fixed neighborhood of one for
large \(N\). Taylor's formula and their logarithms give
\[
 \left|\log\mathsf U_{i,N}(\alpha)\right|
       \le\frac{C_A}{N^2}\sum_{r<i}(r+1)^2
       \le C_A N^{-1/2},
\]
\[
       \mathsf U_{i,N}^{\ \pm1}=1+O_A(N^{-1/2})
                         \qquad(i\le L).
 \tag{24}
\]
The logarithms here are the branches near one, chosen for individual
unit factors; no logarithm of \(\mathsf E_i\) is taken.
The sine denominators likewise give, uniformly for \(i\le L\),
\[
 \begin{split}
 q_{i,N}
 &=\mathsf L_i\,\mathsf U_{i,N}
       [\operatorname{sinc}(\pi/N)
          \operatorname{sinc}(\pi i/N)]^{-1},\\
 q_{N-i,N}
 &=\mathsf H_i\,\mathsf U_{i,N}^{-1}
       [\operatorname{sinc}(\pi/N)
          \operatorname{sinc}(\pi i/N)^3]^{-1}.
 \end{split}
 \tag{25}
\]
The second equality follows first where \(\mathsf E_i\ne0\) from
(4), then everywhere by removable continuation. Both displayed
unit multipliers are \(1+O_A(N^{-1/2})\). For each fixed \(i\),
(23)--(25) prove the locally uniform limits (15)--(16), justifying
the earlier use of (5) to obtain (17).

For sufficiently large \(N\), the two ranges \(1\le i\le L\) and
\(1\le N-i\le L\) are disjoint. Sum (25), using (17):
\[
 \sup_{|\alpha|\le A}
 \left|\sum_{i=1}^{L}
     [q_{i,N}+q_{N-i,N}-\mathsf L_i-\mathsf H_i]\right|
                                      \le C_A N^{-1/2}.
 \tag{26}
\]
The remaining finite and infinite tails are \(O_A(L^{-1})\) by
(13),(17). Since \(L^{-1}=O(N^{-1/2})\), this proves (21).
Apply the estimate on a larger disk and then Cauchy's formula to
obtain its derivative assertion.

## 5. Meaning for the original normal data

In the unscaled original index coordinate,
\(c'(0)=-4(\pi/N)\sin(\pi/N)\). Thus the actual initial common-index
normal satisfies
\[
 c'(0)Q_N(\alpha)
             =-4\pi^2\mathcal Q(\alpha)+O_A(N^{-1/2}),
 \tag{27}
\]
uniformly on the same bounded complex disks. For real \(\alpha\),
its limiting value is strictly negative. This fixes an actual
endpoint datum in the original differentiated recurrence.

The second series in (18) is indispensable: every fixed
\(i=N-m\) contributes at the same \(N^2\) scale as a fixed low
index. In particular a terminating fixed-degree value limit does
not by itself determine (27).

Nothing here compares (27) to the derivative of a chosen moderate
bulk value interpolant. The true bulk defect also includes the
coefficient-shift and propagated endpoint-source contributions.
Its two anchor coefficients, the original trace current, the
external connectors, and any filled-action comparison remain
separate questions. No source coefficient is inferred from the
positive real endpoint constant.

## 6. Direct-source readbacks

Both complete direct sources were read at the displayed unchanged
versions, with the used implications and hashes checked:

* [Original bulk Fourier and complementary Newton identities](research_endpoint_bulk_fourier_interpolation.md),
  SHA256 4f92c6081bf67646a14181bb753a903cf615d16adcd8d56d1534842303adb7eb:
  the ordinary kernel normalization, full physical polynomial,
  and complementary-index identity underlying (4).
* [True endpoint normal and its source placement](research_endpoint_normal_defect_bulk_primitive.md),
  SHA256 60abb9d3e569fae7cd088a752d5f07211a1eeb444ffbd494b376470074ccfec7:
  the original endpoint normal datum, its retained source term,
  and the distinction from scalar bulk compatibility.

The uniform two-ended tail bound, entire limiting series and
quantitative comparison are proved above. Only written mathematics,
source-text reads and hashes were used. No mathematical program,
numerical experiment, test or build was run. Frozen notes and public
manuscripts were not changed.
