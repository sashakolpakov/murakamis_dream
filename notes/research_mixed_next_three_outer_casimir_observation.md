# The remaining transfer as one polynomially weighted radical trace

Private source deduction, 8 November 2026. The outgoing observation
can now be bounded as a polynomial on the full real spectral
interval. Restoring the previously bounded small internal indices
then writes the entire unresolved term as a single original
radical trace. Its insertion has degree less than \(N/3\).

The resulting trace still needs an estimate. The point of the
reduction is to specify that estimate in a fixed original linear
functional, without an unknown analytic interpolation, omitted
normal derivative, or discarded amplitude error.

## 1. The outgoing polynomial on the full spectral interval

Use the actual complete reference of
[the weighted outgoing theorem](research_mixed_next_middle_weighted_outgoing_kernel.md):
a word in powers three and four beginning \(343\), of length at
least five, with outside values \(w=-2\) and \(Z=Z_*\). Write
\[
 \mathcal P_*=\mathcal P_0^+(-2,z_*),\qquad
 \Lambda=\Re\mathcal P_*>419/200,
 \qquad B_0=2383/1500,\qquad B_f=77/50+\pi/50 .
 \tag{1}
\]
The original selected geometric integral remains
\[
 I_{{\rm geom},N}
   =N^{-2}\mathcal A_0e^{N\mathcal P_*}(1+O(N^{-1})),
 \qquad \mathcal A_0\ne0.
 \tag{2}
\]
The formula (2) is for that specified integral, not yet for
the complete transfer.

Put
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 \kappa=q^{D^2/2},\\
 M=\lceil N/2\rceil,\quad U=D-M,\quad L=\lfloor N/6\rfloor,\quad
 d=U-L<N/3,\quad K=\lfloor N/4096\rfloor,\\
 P_k=(r;r)_k,\quad p_k(Z)=(rZ;r)_k,\quad
 Y_N=r^M,\quad c_j=2\cos((2j+1)\pi/N).
\end{gathered}                                                     \tag{3}
\]
The symbol \(d\) is a degree, not the forced interpolation
polynomial in the original transfer.

Let \(\mathscr A_N(\xi,T)\) be the exact polynomial of
[the all-Casimir amplitude theorem, equation (2)](research_mixed_next_middle_casimir_polynomial_amplitude.md).
It has degree at most \(d\) in each variable. At the physical
values it satisfies exactly
\[
 \mathscr A_N(c_j,e^{2\pi ik/N})
                =\mathfrak G_N(j/N,k/N).
 \tag{4}
\]
Define two ordinary polynomials in the spectral variable \(\xi\):
\[
\begin{split}
 H_N^{\rm all}(\xi,Z)
   &=\sum_{k=0}^{U}
      \frac{Y_N^{-k}p_k(Y_N)p_k(Z)}{P_k^2}
                  \mathscr A_N(\xi,e^{2\pi ik/N}),\\
 H_N(\xi,Z)
   &=\sum_{k=K+1}^{U}
      \frac{Y_N^{-k}p_k(Y_N)p_k(Z)}{P_k^2}
                  \mathscr A_N(\xi,e^{2\pi ik/N}).
\end{split}                                                       \tag{5}
\]
Their degrees in \(\xi\) are at most \(d\), and their values
at \(\xi=c_j\) are the literal weighted outgoing sums of
that theorem. In particular this definition does not interpolate
a list of approximate values.

Set
\[
                       E_*=\Lambda-B_0-1/50.
 \tag{6}
\]

**Proposition 1.** For every \(\tau>0\), uniformly at both level
parities,
\[
 \sup_{-2\le\xi\le2}
       \bigl(|H_N^{\rm all}(\xi,Z_*)|+|H_N(\xi,Z_*)|\bigr)
       \le C_\tau N^{A_\tau}e^{N(E_*+\tau)} .
 \tag{7}
\]
A fixed complex neighborhood of \([-2,2]\), depending on \(\tau\),
has the same estimate with any prescribed additional positive
rate allowance. Every fixed spectral derivative has that estimate
on a smaller neighborhood. Moreover, at every angular height,
\[
 |H_N^{\rm all}(2\cos(\theta+i\sigma),Z_*)|
       +|H_N(2\cos(\theta+i\sigma),Z_*)|
 \le C_\tau N^{A_\tau}
                  e^{N(E_*+\tau)+d|\sigma|},
 \qquad \theta,\sigma\in\mathbb R .
 \tag{8}
\]

*Proof.* The all-Casimir amplitude theorem gives on the whole
real interval, including its endpoints,
\[
 |\mathscr A_N(\xi,e^{2\pi it})|
 \le C N^A e^{(2\pi N/3)(-\Im t)_+},
 \qquad 0\le\Re t\le1/2 .
 \tag{9}
\]
It also gives this estimate on a fixed complex spectral tube
with any prescribed extra rate allowance.

We apply the written proof of the weighted outgoing theorem
with (9) in place of its amplitude bound. This changes its
fixed constant to a polynomial in \(N\); it makes no change
to a contour, phase, or exponential comparison. More explicitly,
its low physical rows use only the bound on the real grid.
The main height \(h_+=\max(h_t,0)\), upper aliases and both
unweighted joins use only the bound at nonnegative height.
The two lower sides use exactly the debit
\((2\pi/3)(-\Im t)_+\), leaving their proved decrease
\(7\pi/30\) per unit downward height. The lower horizontal
has the same positive reserve \(37\pi/1500\). The exact
prewall cut, the original \(+N\) measure, and the full
cotangent remainders are unchanged. All these estimates are
uniform in the auxiliary spectral variable because (9) is.
This proves the estimate for \(H_N^{\rm all}\) in (7).

Its removed rows \(0\le k\le K\) have absolute sum at most
\(C N^A e^{N/200}\), by the same positive finite-product
estimate as in the weighted outgoing proof. The action floor
in (1) gives
\[
 E_*>\frac{1459}{3000}>\frac1{200},
\]
so subtraction proves (7) for \(H_N\). No estimate for a
partial signed sum is inferred from a bound for the whole.

For the angular assertion, expand either degree-at-most-\(d\)
polynomial \(H\) as
\[
 H(\xi)=\sum_{a=0}^{d}h_a T_a(\xi/2),\qquad
 |h_0|\le\|H\|_{[-2,2]},\quad
 |h_a|\le2\|H\|_{[-2,2]}\ (a\ge1).
 \tag{10}
\]
These coefficient bounds follow from cosine orthogonality,
also for complex coefficients. The exact identity
\(T_a(\cos(\theta+i\sigma))=\cos(a(\theta+i\sigma))\)
bounds each term by \(e^{a|\sigma|}\). Summing at most
\(d+1\) terms proves (8). The fixed-tube conclusion follows
either from the complex version of (9) in the same outgoing
proof or from the Chebyshev ellipse estimate. Cauchy's formula
on a smaller tube gives the fixed derivative statement. \(\square\)

## 2. Restoring the small internal indices

Keep the original Newton polynomials and trace
\[
 e_a(x)=S_a^{-2}\prod_{h<a}(c_h-x),\qquad
 S_a=\prod_{\nu=1}^a2\sin(\pi\nu/N),
\]
\[
 K_N^{\rm ord}(w,x)=\sum_{a=0}^{D}e_a(w)e_a(x),\qquad
 \mathcal K_{3,N}(w,x)
   =\phi_N^{(t)}
      [\mathcal R_N(t)^3K_N^{\rm ord}(w,t)K_N^{\rm ord}(x,t)] .
 \tag{11}
\]
All traces are the original full Hermite traces, with their
first normals at double roots. Put
\[
 \mathcal L_N(P)=
   \phi_N^{(x)}
     [\mathcal R_N(x)^3e_M(x)\mathcal K_{3,N}(-2,x)P(x)]
 \tag{12}
\]
for an ordinary polynomial \(P\). This functional is independent
of the outgoing reference \(Z_*\).

**Proposition 2.** For some fixed \(\epsilon_*>0\),
\[
 \boxed{\quad
 \mathcal T_0[F_N](-2,Z_*)=
 I_{{\rm geom},N}
   +\frac{(-q)^M}{\kappa^2N}\,
                      \mathcal L_N(H_N(\cdot,Z_*))
   +O(e^{N(\Lambda-\epsilon_*)}).
 \quad}                                                         \tag{13}
\]
The transfer on the left retains its original two Fourier
coefficients. Formula (13) does not assert smallness of its
displayed radical trace.

*Proof.* The exact restored source of
[the restored-middle theorem](research_mixed_next_three_restored_middle_large_indices.md)
is the sum over
\[
 \lceil N/2\rceil\le b<\lceil5N/6\rceil,\qquad
 j>\lfloor N/64\rfloor,\qquad k>K,\qquad j,k\le D-b .
\]
The [small internal-index theorem](research_mixed_next_three_small_internal_indices.md)
bounds the complementary triples \(j\le\lfloor N/64\rfloor\),
\(k>K\), over this whole physical band, at rate
\(419/200-1/32<\Lambda-1/32\). Restore that entire complementary
sum with an exponentially small error. The old filter corrections
remain separate and are not decomposed again.

The exact factorization in the weighted outgoing theorem,
equations (30)--(32), then writes the restored term as
\[
 \frac{\kappa(-q)^Dq^{-U}}N
 \sum_{j=0}^{U}
    s_{2j+1}q^{3j(j+1)}A_{j,N}
        \mathcal K_{3,N}(-2,c_j)H_N(c_j,Z_*),
 \tag{14}
\]
where \(s_a=2\sin(\pi a/N)\) and
\[
 A_{j,N}=\frac{S_U^2}{S_{U-j}S_{U+j+1}}
 =\begin{cases}
 1/2,&N=2m,\\
 s_{m-j}/\{4\cos^2(\pi/(2N))\},&N=2m+1.
 \end{cases}                                                     \tag{15}
\]
Both parities have \(U=m-1\). No parity-dependent endpoint
factor is approximated in (15).

The full radical contraction, applied with \(D-U=M\), gives
\[
 \phi_N[e_M f]=\sum_{j=0}^{U}b_{Uj}f(c_j),\qquad
 b_{Uj}=(-1)^{U+j}s_{2j+1}A_{j,N}.
 \tag{16}
\]
This is the original consumed normal. Multiplying by the exact
crossing value
\[
 \mathcal R_N(c_j)^3
       =\kappa^3(-1)^j q^{3j(j+1)}
\]
shows that the sum in (14) equals
\((-1)^U\kappa^{-3}\mathcal L_N(H_N)\). Its full scalar is
therefore
\[
 \frac{\kappa(-q)^Dq^{-U}}N(-1)^U\kappa^{-3}
                 =\frac{(-q)^M}{\kappa^2N},
 \tag{17}
\]
using \(D-U=M\). This proves (13), with, for example,
\(\epsilon_*=\tfrac12\min(\epsilon_{\rm both},1/32)\)
after absorbing the fixed polynomial cost.

The polynomial \(e_MH_N\) has degree at most
\(M+d=D-L<N\). Thus its formation itself requires no
reduction modulo the spectral relation. The original trace
still performs its prescribed reduction on the complete
product in (12). Since \(e_M\) vanishes at every distinct
physical node, its derivative consumes the required normal;
this does not drop the inner normals in \(\mathcal K_{3,N}\)
or replace \(\phi_N\) by a new positive trace. \(\square\)

## 3. A precise remaining Fourier estimate

Define the original mode responses
\[
 \mathcal L_{N,a}=\mathcal L_N(T_a(\cdot/2)),
                         \qquad 0\le a\le d .
 \tag{18}
\]
If \(H_N(\xi,Z_*)=\sum_{a=0}^{d}h_{a,N}T_a(\xi/2)\), then
\[
 \mathcal L_N(H_N)=\sum_{a=0}^{d}h_{a,N}\mathcal L_{N,a}
 \tag{19}
\]
exactly. Hence
\[
 |\mathcal L_N(H_N)|
 \le (2d+1)\|H_N(\cdot,Z_*)\|_{[-2,2]}
                      \max_{0\le a\le d}|\mathcal L_{N,a}|.
 \tag{20}
\]
Equations (7),(13),(18)--(20) isolate an explicit sufficient
estimate: a uniform bound
\[
 \max_{0\le a\le U-L}|\mathcal L_{N,a}|
                    \le C N^B e^{NB_f}
 \tag{21}
\]
would suppress the remaining trace at this base reference.
Indeed
\[
 B_f-B_0<149/10500,\qquad
 1/50-(B_f-B_0)>61/10500.
\]
Use (7) with \(\tau=1/1000\), and retain the original
factor \(1/N\) in (13). The right side of (20) would then
have a fixed strict gap below \(\Lambda\). Combined with (2),
this would yield the complete local transfer asymptotic.

**Estimate (21) is not proved here.** It is stronger than a
bound on the single response \(a=0\). Its modes retain the
outer radical normal and the inner full signed trace.
A proof for the old charge-one terminal contour cannot be
applied to these different source functions without checking
their phases and all boundary terms.

Nor is (21) asserted to be necessary. The actual coefficients
\(h_{a,N}\) may permit a sharper estimate of the weighted sum
(19) than the maximum used in (20). Failure of that sufficient
uniform bound would not disprove suppression of the actual
source.

The conclusions proved here are (7), (8) and the exact
reduction (13). They supply no full transfer noncancellation,
arbitrary-short composition theorem, or finite-exceptions
result. No mathematical numerical evaluation was used.

