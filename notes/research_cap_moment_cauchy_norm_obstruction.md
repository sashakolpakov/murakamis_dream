# An exponential obstruction to the bare cap-moment Cauchy estimate

31 October 2026. Workspace analytical research lemma. The complete
proof and original-source scope received independent internal analytical
reviews by the root and coherent agents, both PASS. This concerns the exact original-demand cap/CROSS convolution
at even levels. It disproves one proposed positive-norm strengthening,
not the signed convolution comparison, a shared-source estimate, or a
volume conjecture. No numerical growth test is an input to the proof.

## 1. The original coefficient and the particular proposed norm bound

Use the exact source in
[original-demand cap/CROSS convolution](research_two_port_main_cap_original_demand_convolution.md):
the adjacent ordered quartets are
\[
 E=(A,0,C,Z),\qquad F=(0,A,0,C),
\]
with the two original protected faces specialized to zero. The ordinary
face \(A\) occurs only at these two ports, so its degree \(d=N-1\)
is extracted first. The CROSS coupon at \(E\) is evaluated at \(-2\)
and the RIGHT coupon at \(F\) at \(+2\). Keep
\[
 N=2m,\quad M=m-1,\quad \theta=\pi/N,\quad
 s_r=2\sin(r\theta),\quad
 a_r=4\cos^2((r+\tfrac12)\theta).
\]
The original positive endpoint continuant and its unused factors are
\[
 \begin{split}
 K_0&=1,\qquad K_1=s_1^2(A+Z),\\
 K_r&=s_r^2(A+Z)K_{r-1}
       +s_rs_{r-1}a_{r-1}AZK_{r-2},\\
 C_{j,h}&=[A^jZ^{d-h-j}]K_{d-h}
                     \prod_{r=d-h+1}^{d}a_r.
 \end{split}                                                    \tag{1}
\]
For \(0\le n\le d-1\), the actual remaining coefficient is, up to
the common raw sign \((-1)^d\),
\[
 S_{N,n}=\sum_{j\in J_n}(-1)^jU_jC_{j,n-j},\qquad
 D_{N,n}=\sum_{j\in J_n}V_jC_{j,n-j}>0,
 \quad J_n=[\max(0,n-M),\min(M,n)]\cap\mathbb Z,                 \tag{2}
\]
where the endpoint comparator is \(D_{N,n}\), and
\[
 \begin{split}
 U_j&=\csc^2(\theta/2)
       \prod_{r=1}^{j}\frac{\sin^2(r\theta)}
                              {\sin^2((r+\tfrac12)\theta)},\\
 V_j&=\sec^2(\theta/2)
       \prod_{r=1}^{j}\frac{\sin^2(r\theta)}
                              {\cos^2((r+\tfrac12)\theta)}.
 \end{split}                                                    \tag{3}
\]
The degree \(A^d\), both remaining degrees \(C^nZ^{d-n}\), every
unused row in (1), and the genuine RIGHT/CROSS cutoffs are unchanged.

The positive moment theorem
[positive cap-moment theorem](research_flat_cap_positive_moment_form.md) constructs a positive
random variable \(X_N\) with \(U_0\mathbb E X_N^j=U_j\) through
degree \(d\). Set
\[
 F_{N,n}(t)=\sum_{j\in J_n}C_{j,n-j}t^j,\qquad
 \mathcal L_N(p)=U_0\mathbb E p(X_N).
\]
Thus \(S_{N,n}=\mathcal L_N(F_{N,n}(-t))\). The bare moment-Cauchy
upper bound is
\[
 |S_{N,n}|\le \mathcal N_{N,n},\qquad
 \mathcal N_{N,n}
  :=\sqrt{U_0\mathcal L_N(F_{N,n}(-t)^2)}
   =U_0\sqrt{\mathbb E F_{N,n}(-X_N)^2}.                         \tag{4}
\]
Its square is finite because \(\deg F_{N,n}\le M\) and
\(2M=d-1\). The proposed strengthening
\(\mathcal N_{N,n}\le C N^kD_{N,n}\), uniformly in \(N,n\), is
false. More precisely, with
\[
 f(t)=-\int_0^t\log\tan(\pi s)\,ds
     =\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi},
 \quad 0\le t\le\tfrac12,
\]
for every fixed \(u\in(0,1/4]\) and every sequence of even levels
and original degrees satisfying \(N\to\infty\) and \(n/N\to u\),
we prove
\[
 \boxed{
 \liminf_{N\to\infty}
  \frac1N\log\frac{\mathcal N_{N,n}}{D_{N,n}}
  \ \ge\ \chi(u):=4f(u/2)-2f(u)-k(u)>0,\qquad
 k(u)=2\int_0^u\log(2\cos(\pi t))\,dt.}
                                                                  \tag{5}
\]
This is an obstruction with the original face demand already imposed.
The open comparison \(|S_{N,n}|\le C N^kD_{N,n}\) is not contradicted:
the signed expectation in (4) can be much smaller than its norm.

## 2. A single exact orthogonal projection

The beta-product construction can be split into two independent copies:
\(X_N=Y_NY_N'\), where
\[
 w_j=\mathbb E Y_N^j=\sqrt{U_j/U_0},\qquad
 \frac{w_j}{w_{j-1}}
     =\frac{\sin(j\theta)}{\sin((j+\tfrac12)\theta)}.             \tag{6}
\]
All moments used below have degree at most \(d\). Let
\(\ell_N(p)=\mathbb E p(Y_N)\). For completeness, the exact
orthogonal polynomials used here follow directly from these moments.
On polynomials of degree at most \(M\), with \(D=t\partial_t\), set
\[
 T=t^{-1}(\cos(2\theta D)-1)
                        -\cos(\theta(2D+\tfrac12)).
\]
The first numerator annihilates constants. Writing
\(A_j=\cos(2j\theta)-1\),
\(B_j=-\cos((2j+\tfrac12)\theta)\), its monomial action is
\(Tt^j=A_jt^{j-1}+B_jt^j\). The exact sine ratio (6) gives
\[
 (A_i-A_j)w_{i+j-1}+(B_i-B_j)w_{i+j}=0.
\]
Thus \(T\) is symmetric for \(\ell_N\). The eigenvalues
\(B_0,\ldots,B_M\) are distinct, and its eigenpolynomials \(P_r\),
normalized by \(P_r(0)=1\), are orthogonal. Coefficient comparison
gives
\[
 \frac{[t^{j+1}]P_r}{[t^j]P_r}
   =-\frac{\sin((r+j+\tfrac12)\theta)\sin((r-j)\theta)}
            {\sin^2((j+1)\theta)}.
\]
Consequently their leading coefficients and squared norms are
\[
 \kappa_r=[t^r]P_r
  =(-1)^r\frac{\prod_{a=r}^{2r-1}\sin((a+\tfrac12)\theta)}
                  {\prod_{a=1}^{r}\sin(a\theta)},\qquad
 g_r=\ell_N(P_r^2)
  =\frac{\sin(\theta/2)}{\sin((2r+\tfrac12)\theta)}.             \tag{7}
\]
Here empty products give \(\kappa_0=g_0=1\). One direct verification
of the norm formula is the multiplication recurrence
\(tP_r=\mathcal A_rP_{r+1}+\mathcal B_rP_r+
\mathcal C_rP_{r-1}\), whose leading coefficients and value at zero
give
\[
 \mathcal A_r=-\frac{\sin((r+1)\theta)\sin((r+\tfrac12)\theta)}
                       {\sin((2r+\tfrac12)\theta)
                        \sin((2r+\tfrac32)\theta)},\qquad
 \mathcal C_r=-\frac{\sin(r\theta)\sin((r-\tfrac12)\theta)}
                       {\sin((2r-\tfrac12)\theta)
                        \sin((2r+\tfrac12)\theta)}.
\]
Symmetry then gives
\(g_r/g_{r-1}=\mathcal C_r/\mathcal A_{r-1}
=\sin((2r-\tfrac32)\theta)/\sin((2r+\tfrac12)\theta)\),
which telescopes to (7). For the indices needed below, eventually
\(r\le n<M\), since \(n/N\to u\le1/4\). Thus no polynomial beyond the finite Hilbert
degree is needed. These are the single-factor polynomials, not the
different Jacobi polynomials of the source continuant.

Now take any sequence specified in (5), at sufficiently large \(N\).
Then \(n<M\), so the original range
is exactly \(J_n=\{0,\ldots,n\}\), not a replacement cutoff.
In the positive tensor metric \(\ell_N\otimes\ell_N\), project
\(F_{N,n}(-tu)\) onto \(P_n(t)\otimes1\). Orthogonality removes
every \(j<n\), while
\(\ell_N(t^nP_n)=g_n/\kappa_n\). Therefore
\[
 \langle F_{N,n}(-tu),P_n(t)\otimes1\rangle
   =(-1)^n C_{n,0}w_n\frac{g_n}{\kappa_n},
\]
and a single orthogonal projection gives the exact bound
\[
 \boxed{\mathcal N_{N,n}
       \ge U_0 C_{n,0}\frac{w_n\sqrt{g_n}}{|\kappa_n|}.}          \tag{8}
\]
This projection is unaffected by any cancellation among the other
tensor components. It uses no condition-number estimate for the
monomial-to-orthogonal basis change.

The remaining factors in (8), apart from \(C_{n,0}\) and
\(\kappa_n\), have zero exponential rate. The literal sine product
gives, for \(j\le M\),
\[
 4\cos^2(\theta/2)\le U_j\le\csc^2(\theta/2)\le N^2,
 \qquad N^{-1}\le g_j\le1.
                                                                  \tag{9}
\]
For the lower bound on \(U_j\), compare each denominator sine to
\(\sin((r+1)\theta)\) and telescope; all the angles are at most
\(\pi/2\). In particular \(w_n\ge\sqrt3/N\), and none of these
factors can hide an exponential loss.

## 3. The exact endpoint comparator rate

The uniform closed endpoint coefficient theorem in
[uniform half-block and triangle coefficient theorem](actual_fejer_half_block_entropy.md) and
[continuous full-kernel coefficient theorem](actual_fejer_full_kernel_entropy_identity_reduction.md)
applies to the actual coefficients (1). On a triangle of total load
\(1/2\), its entropy is the sum of \(f\) at the three corner loads.
The CROSS rate is the maximum of the sum over its two genuine
triangles, with one shared outer split. Finite forced degree shifts
and polynomial scalar factors are already covered by that uniform
closed theorem.

For \(n/N\to\rho\le1/4\), \(j/N\to v\), the endpoint cap has
\(N^{-1}\log V_j\to-2f(v)\). The CROSS coefficient in (1) has
limiting loads
\((v,0,\rho-v,1-\rho)\). Write the first outer split as \(a\).
The two triangle entropies give the combined rate
\[
 E_\rho(a,v)=2f(a)+f(v-a)+f(\rho-v)+f(\rho-a)-2f(v),
 \qquad 0\le a\le v\le\rho.                                  \tag{10}
\]
The uniform closed coefficient theorem and the polynomial number of
terms in (2) imply that the rate of \(D_{N,n}\) is the maximum in
(10), along any such sequence. The \(d=N-1\) versus \(N\)
normalization changes the arguments by \(O(1/N)\); continuity
handles it. At limiting \(\rho=1/4\), one does not need the
finite ratio \(n/d\) to be at most \(1/4\).

We prove the elementary maximum identity
\[
 \max_{0\le a\le v\le\rho}E_\rho(a,v)=2f(\rho),
 \qquad 0<\rho\le\tfrac14.                                    \tag{11}
\]
On this interval \(f\) is nonnegative, increasing and concave.
The three boundary edges satisfy
\[
 \begin{array}{ll}
 a=0:&E=f(\rho-v)+f(\rho)-f(v)\le2f(\rho),\\
 a=v:&E=2f(\rho-v)\le2f(\rho),\\
 v=\rho:&E=2[f(a)+f(\rho-a)-f(\rho)]
                \le4f(\rho/2)-2f(\rho)\le2f(\rho).
 \end{array}
\]
Equality occurs at \(a=v=0\). There is no critical point in the
open triangle. Indeed put
\(z=\tan(\pi v)\), \(p=\tan(\pi\rho)\),
\(u=\tan(\pi a)\). The two critical equations are
\[
 u^2=\frac{(z-u)(p-u)}{(1+zu)(1+pu)},\qquad
 \frac{z-u}{1+zu}=z^2\frac{p-z}{1+pz}.
\]
Let \(r=p-z\), so \(0<r<1\). The second equation forces
\(u=z/(1+rz)\). Substituting into the first forces
\[
 1+2rz+z^2=r^2(1+rz)^2.
\]
But the left side minus the right side is
\[
 (1-r^2)\bigl[1+2rz+(1+r^2)z^2\bigr]>0.
\]
This contradiction proves (11), since every interior maximum of the
smooth function would be critical. Compactness and the displayed
boundary checks include all corners.

It follows, along the sequences in (5), that
\[
 \lim_{N\to\infty}\frac1N\log D_{N,n}=2f(u).                  \tag{12}
\]
The lower bound can also be seen without a coefficient limit:
the original \(j=0\) term has
\[
 C_{0,n}=N^2\prod_{h=0}^{n-1}
       \frac{\cos^2((h+\tfrac12)\theta)}{\sin^2((h+1)\theta)},
\]
whose logarithmic rate is \(2f(\rho)\), while \(V_0\) has zero
rate. Thus the maximizing boundary term is genuinely present in the
original finite sum.

For the numerator projection, \(C_{n,0}\) has both middle loads
zero and total outer load \(n/d\to u\). Its two endpoint
triangles maximize \(2f(a)+2f(u-a)\) at \(a=u/2\). Hence
\[
 \lim_{N\to\infty}\frac1N\log C_{n,0}=4f(u/2).                \tag{13}
\]
The lower bound here is specifically the positive endpoint coefficient
lower theorem, not the later sharp spectral limsup majorant. To see
its application directly, the original coefficientwise comparison
(15) of [uniform half-block and triangle coefficient theorem](actual_fejer_half_block_entropy.md) specializes at both
middle variables zero to
\[
 4(A+Z)D_0(A,Z)^2\ \le\ K_d(A,Z)
             \ <\ 12(A+Z)D_0(A,Z)^2.
\]
The actual \(D_0\) coefficients have the uniform closed triangle
rate \(2f(a)\), including this protected-middle face. Choose a genuine
integer split of the desired outer degree within a bounded distance
of \(n/2\), and retain either forced outer term \(A\) or \(Z\).
The positive convolution supplies the lower rate in (13); concavity
and its polynomial number of terms supply the matching upper rate.
The forced outer unit and each degree \(M=N/2-1\) cause only bounded
degree offsets, covered by the closed coefficient theorem. Thus (13)
uses the original continuant coefficient, not an auxiliary
unconditioned face polynomial or an unproved spectral lower estimate.

## 4. A strictly positive excess and its precise limitation

The explicit product (7) yields
\[
 \lim_{N\to\infty}\frac1N\log|\kappa_n|
  =\int_u^{2u}\log\sin(\pi t)\,dt
       -\int_0^u\log\sin(\pi t)\,dt
  =k(u).                                                        \tag{14}
\]
For the last equality, rewrite the difference as
\(\int_0^{2u}\log\sin(\pi t)\,dt
-2\int_0^u\log\sin(\pi t)\,dt\), then use sine doubling.
The endpoint logarithm is integrable; upper and lower sums on the
two monotonicity intervals, with its first cell integrated directly, justify these
shifted Riemann sums. The error from the finite products to the same
integrals with endpoint \(n/N\) is \(O(\log N/N)\); continuity
then handles arbitrary \(n/N\to u\), including integer floors.
Combining (8), (9), and (12)--(14) proves the lower bound in (5).

The excess is strictly positive by a direct derivative identity.
It is continuous at zero with \(\chi(0)=0\), and
\[
 \begin{split}
 \chi'(u)
  &=2f'(u/2)-2f'(u)-2\log(2\cos(\pi u))\\
  &=2\log\frac{1+\cos(\pi u)}{2\cos^2(\pi u)}>0
        \qquad(0<u\le1/4).
 \end{split}                                                    \tag{15}
\]
Indeed if \(c=\cos(\pi u)\), then
\(1+c-2c^2=(1-c)(2c+1)>0\). At \(u=1/4\), reflection in
(14) also gives \(k(1/4)=f(1/4)\), recovering the special value
\(\chi(1/4)=4f(1/8)-3f(1/4)>0\). No rational or numerical
evaluation of special values is required. On each compact subinterval
of \((0,1/4]\), (15) gives a positive lower bound for this excess;
no uniform positive bound as \(u\downarrow0\) is asserted.

The constant-tensor component \(\langle F(-tu),1\otimes1\rangle\)
is the signed coefficient divided by \(U_0\). The large component
used in (8) lies instead in the orthogonal direction
\(P_n\otimes1\). Its growth cannot be removed from the positive
norm, but it contributes zero to that constant-tensor expectation.
More explicitly, if
\(F_{N,n}(-tu)=\sum_{a,b}d_{a,b}P_a(t)P_b(u)\), then
\[
 d_{n,0}=(-1)^n C_{n,0}w_n/\kappa_n,\qquad
 d_{0,0}=S_{N,n}/U_0.
\]
Since \(g_n\) has zero exponential rate, the same proof gives
\(\liminf N^{-1}\log(U_0|d_{n,0}|/D_{N,n})\ge\chi(u)>0\).
Thus even a single coefficient defeats a polynomial comparison with
the absolute coefficient sum or Euclidean coefficient norm in this
fixed explicit basis. This is not a claim about every possible basis,
and supplies no lower bound for the distinct coefficient \(d_{0,0}\).
Consequently this proof explains precisely why a bare Cauchy step
can lose exponential information. It leaves open a cancellation-aware
operator identity or estimate for the original signed expectation.
It does not show that any actual shared coefficient exceeds its
endpoint rate, nor does it change the original source or its cutoffs.

## Proof inputs and validation scope

The exact source (1)--(3), the positive beta moments, and the uniform
closed endpoint coefficient limits have already received independent
internal proof reviews. The single-factor tensor construction and
norms (6)--(7) are also derived in
[actual continuant and cap tensor metric](research_cap_demand_continuant_jacobi_interface.md), §§6--7;
the algebra needed here is stated explicitly above. The new inputs are
the single-component lower bound (8), the elementary maximization
(11), and their consequence (5). The root and coherent agents independently completed full analytical
reviews of those new steps, the original degree restrictions, and the
exact source normalization, both PASS. No finite numerical sampling is offered as proof of
the asymptotic obstruction.
