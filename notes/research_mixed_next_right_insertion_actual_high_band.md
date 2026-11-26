# An actual-output norm budget for the high right insertion

Private research deduction, 8 November 2026. The actual output-height
bound permits a complete estimate of the part of the right paired
insertion with physical index at least \(5N/6\). This enlarges the
previously paid band \(b\ge8N/9\). The estimate is an exponential
budget for the coherent insertion on the full terminal trace strip,
not a polynomial-norm assertion. Its complete terminal observation
is strictly below the original next-three action.

The residual insertion, both Fourier alternatives, and every vertical
and half-grid current remain explicit. No numerical evaluation or
change to a frozen source is used.

## 1. Exact original source and actual domain

Use precisely the conventions of
[the closed right paired reduction](research_mixed_next_right_paired_terminal_insertion.md):
\[
\begin{gathered}
D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
P_j=(r;r)_j,\quad S_j=|P_j|,\quad p_j(Z)=(rZ;r)_j,\\
\kappa=q^{D^2/2},\quad
c_j=2\cos((2j+1)\pi/N),\quad
e_j(t)=S_j^{-2}\prod_{a<j}(c_a-t),\\
K_N^{\rm ord}(z,t)=\sum_{j=0}^{D}e_j(z)e_j(t),\qquad
A_3=JM^3,\quad \ell_b(w)=(v(w)^TA_3^2)_b .
\end{gathered}                                                    \tag{1}
\]
Here \(q\) is the quantum parameter. The next kernel is the original
own-three kernel
\[
C_{0,N}(Y,Z)=\sum_{k=0}^{D}
       \frac{Y^{-k}p_k(Y)p_k(Z)}{P_k^2}.                         \tag{2}
\]
In particular the incoming carrier is retained.

The actual family consists of complete words in powers three and
four, beginning \(343\), of length \(m\ge5\), with the original
matched output \(Z=e^{-2\pi iz_*}\). The
[correlated-height theorem, Section 3](research_mixed_cap_343_correlated_height_bounds.md)
gives
\[
                 \frac45<|Z|<\frac87.                         \tag{3}
\]
Only the upper bound is used in the estimate below. We prove the
finite norm bound on the larger disk \(|Z|\le8/7\). We do not infer
that this disk is an actual output image.

Keep the old filter and its thresholds
\[
M_N=\lceil N/2\rceil,\qquad B_N=\lceil11N/12\rceil,
\qquad Q_N=\lceil5N/6\rceil.                                  \tag{4}
\]
The letter \(Q_N\) in this note is only an integer threshold, not
the physical Chebyshev relation. For any subset
\(I\subset\{Q_N,\ldots,D\}\), define the original coherent
insertion
\[
\begin{split}
\mathcal I_{0,N}^{I}(t,Z)
  =\sum_{b\in I}(-q)^b C_{0,N}(r^b,Z)
       \sum_{j=0}^{D-b}b_{D-b,j}\mathcal R_N(c_j)^3
                                      K_N^{\rm ord}(c_j,t),\\
b_{nj}=(-1)^{n+j}
 \frac{2\sin((2j+1)\pi/N)S_n^2}{S_{n-j}S_{n+j+1}},\qquad
|b_{nj}|\le2,\quad |\mathcal R_N(c_j)|=1 .
\end{split}                                                     \tag{5}
\]
All phases in (5) are the original ones. The high-Newton contraction
in the cited reduction proves this formula including the consumed
normal and the absence of the odd simple-node term. Its separate
degrees in \(t,Z\) are at most \(D-Q_N<N/6\).

## 2. The complete insertion on the terminal strip

Let
\[
J(u)=\int_0^u\log(2\sin\pi s)\,ds,
\qquad
\|I\|_{\rm strip}
 =\sup_{-\pi\le\Re\theta\le\pi,\ |\Im\theta|\le\log2}
                       |I(-2\cos\theta)| .                   \tag{6}
\]
The original uniform sine-factorial estimate is
\(\log S_j=NJ(j/N)+O(\log N)\), including \(j=0\).
The elementary bounds already proved in
[the seam collar, Section 2](research_mixed_next_complete_source_seam_collar.md)
and [the terminal insertion estimate](research_mixed_next_high_coefficients_terminal_insertion.md)
are
\[
                -2J(1/6)<\frac{13}{40},\qquad
                \log3<\frac{11}{10}.                         \tag{7}
\]

The following extension of the latter insertion estimate uses no
new contour. For \(0\le\ell\le j<N/6\), physical termination gives
\[
\begin{split}
K_N^{\rm ord}(c_j,-2\cos\theta)
 &=\sum_{\ell=0}^j e_\ell(c_j)e_\ell(-2\cos\theta),\\
0\le e_\ell(c_j)
 &=\prod_{k=0}^{\ell-1}
 \frac{\sin(\pi(j-k)/N)\sin(\pi(j+k+1)/N)}
      {\sin^2(\pi(k+1)/N)}
 \le\binom j\ell\binom{j+\ell}{\ell}.
\end{split}                                                     \tag{8}
\]
To check the enlarged index domain, reorder the first numerator
product into increasing order. Both comparisons then pair a sine
at a larger positive integer with its smaller denominator index.
The decrease of \(\sin x/x\) on \((0,\pi)\) proves each inequality;
all indices are at most \(2j<N/3\). Therefore
\[
\sum_{\ell=0}^j e_\ell(c_j)\le6^j.                            \tag{9}
\]
On the strip (6), each numerator factor of
\(e_\ell(-2\cos\theta)\) has modulus at most \(9/2\).
Every sine factor through index \(j<N/6\) is less than one,
so \(S_\ell\ge S_j\). Hence
\[
\|K_N^{\rm ord}(c_j,\cdot)\|_{\rm strip}
       \le\frac{27^j}{S_j^2}
       \le CN^A\exp\{N E(j/N)\},\qquad
E(u)=u\log27-2J(u).                                           \tag{10}
\]
The function \(E\) increases on \([0,1/6]\), because
\(2\sin\pi u\le1\) there. Equations (7) imply
\[
              E(1/6)<\frac{11}{20}+\frac{13}{40}
                         =\frac78.                           \tag{11}
\]
This is an upper bound for the entire ordinary polynomial in (8),
not an asymptotic assigned to one of its terms.

## 3. The original terminating next kernel

For \(b\ge Q_N\), put \(n=D-b<N/6\). At the physical node
\(Y=r^b\), exactly the rows \(0\le k\le n\) survive in (2).
Their incoming carrier has modulus one, and reflection gives
\[
\frac{|p_k(r^b)|}{S_k}
   =\frac{S_n}{S_{n-k}S_k}\le\binom nk .                       \tag{12}
\]
As in (8), this last inequality follows by pairing the increasing
numerator indices \(n-k+1,\ldots,n\) with \(1,\ldots,k\) and
using decreasing \(\sin x/x\). There is no division by a
root-of-unity zero. On \(|Z|\le8/7\), retain the entire outgoing
polynomial and use
\[
|p_k(Z)|\le(15/7)^k,\qquad S_k\ge S_n.
\]
Consequently
\[
\begin{split}
|C_{0,N}(r^b,Z)|
 &\le\frac1{S_n}\sum_{k=0}^n\binom nk(15/7)^k
   =\frac{(22/7)^n}{S_n}\\
 &\le CN^A\exp N\{(n/N)\log(22/7)-J(n/N)\}.
\end{split}                                                     \tag{13}
\]
The last rate increases through \(1/6\). The written positive
exponential-series witness
\[
e^{7/6}>
1+\frac76+\frac{49}{72}+\frac{343}{1296}+\frac{2401}{31104}
 =\frac{99193}{31104}>\frac{22}{7}                             \tag{14}
\]
has final cross-product difference \(10063>0\). Thus (7) gives
\[
\frac16\log(22/7)-J(1/6)
 <\frac7{36}+\frac{13}{80}=\frac{257}{720}.                    \tag{15}
\]
This estimates the full finite next kernel, including its true
row zero and every surviving numerator. Zeros under variation of
\(Z\) are neither discarded nor divided out.

Combining (5), (10)--(15), and the at most \(N^2\) pairs of
indices proves the actual norm budget
\[
\boxed{\quad
\sup_{|Z|\le8/7}\|\mathcal I_{0,N}^{I}(\cdot,Z)\|_{\rm strip}
 \le C_\tau N^{A_\tau}
      \exp N\left\{\frac{887}{720}+\tau\right\},
\quad I\subset\{Q_N,\ldots,D\}.
\quad}                                                        \tag{16}
\]
The definition retains all coherent phases; the estimate is uniform
under taking any subset only because an explicit positive upper
bound has now been proved. No analogous subset estimate is inferred
from a bound on a signed trace.

## 4. Full terminal source and the actual action comparison

The complete terminal insertion operator in
[the right paired theorem, Section 4](research_mixed_next_right_paired_terminal_insertion.md)
applies to (16):
\[
|\phi_N[\mathcal R_N^3K_N^{\rm ord}(w,\cdot)I]|
 \le C_\tau N^{A_\tau} e^{N(M_{\rm term}+\tau)}
                                       \|I\|_{\rm strip},
\qquad M_{\rm term}<\frac{17}{20}.                            \tag{17}
\]
This input retains every physical wire row, angular value and
normal, both aliases, both wire cuts, angular connectors, and
higher trace charges. The fixed margin between its trace height
and \(\log2\) also controls the required angular derivatives of
the whole insertion. The estimate is valid for all real ordinary
\(w\in[-2,2]\), and with arbitrarily small rate allowance on a
fixed complex neighborhood of \(-2\). It is not a consequence of
the terminal critical value alone.

For completeness, the same argument termwise in the exact
high-Newton contraction gives the positive bound
\[
\sum_{b\in I}
 \left|\frac{(-q)^b}{\kappa^2N}\ell_b(w)C_{0,N}(r^b,Z)\right|
 \le C_\tau N^{A_\tau}
           \exp N\left\{\frac{1499}{720}+\tau\right\}.
                                                               \tag{18}
\]
Indeed (17) applied to each complete insertion (8), followed by
the proved \(|b_{nj}|\le2\), bounds \(\ell_b\) at rate
\(17/20+7/8=69/40\). Adding (15) gives \(1499/720\).
The original scalar \(1/(\kappa^2N)\) has been retained and costs
only a power of \(N\). Both level parities are included.

At the actual ordinary next-three references,
[the stronger action floor, equation (13)](research_mixed_next_three_real_pair_action_floor.md)
gives
\[
\Re\mathcal P_0^+(-2,z_*)>\frac{419}{200},\qquad
\frac{419}{200}-\frac{1499}{720}=\frac{47}{3600}>\frac1{100}.
                                                               \tag{19}
\]
Choose the total rate allowance and the fixed color/output
neighborhoods inside the strict reserve. Since (3) is strict on
the compact actual reference family, those neighborhoods may also
remain inside \(|Z|<8/7\). Equations (18)--(19), with Markov in
the complete ordinary polynomial and Cauchy on smaller fixed
neighborhoods, show that every fixed normalized mixed jet of the
signed finite band is \(O(e^{-N/200})\). Equivalently, one may
differentiate its holomorphic summands before the positive sum in
(18), with the same conclusion and polynomial cost; no derivative
of an absolute value is meant. This normalization uses the original
action and its constants. It makes no assertion about a nonzero
coefficient of this band.

## 5. The resulting paired-right reduction

Let \(\mathscr R_N^{\rm cl}\), \(V_N\), \(J_N^{\rm grid}\), and
\(\mathscr H_N\) have exactly the orientations and original
\(+N\) in equations (11)--(15) of the right paired theorem.
Split its insertion at \(Q_N\), without changing the old filter:
\[
\mathcal I_{0,N}=\mathcal I_{0,N}^{\rm mid}
                      +\mathcal I_{0,N}^{\rm high},\qquad
I_{\rm mid}=\{M_N,\ldots,Q_N-1\},\quad
I_{\rm high}=\{Q_N,\ldots,B_N-1\}.                            \tag{20}
\]
Empty ranges have their usual zero value. The original
first-coordinate deletion is still paid on every physical subset
by its positive rectangle bound \(11/6\), as traced in that source.
It is not subtracted from an absolute estimate of a signed
coefficient. Thus the exact closed-right identity has the form
\[
\mathscr R_N^{\rm cl}
 =\frac1{\kappa^2N}\phi_N[
       \mathcal R_N^3K_N^{\rm ord}(w,\cdot)
                    \mathcal I_{0,N}^{\rm mid}(\cdot,Z)]
       +\mathcal E_N,                                        \tag{21}
\]
where every fixed mixed jet of
\(e^{-N\mathcal P_0^+}\mathcal E_N\) is \(O(e^{-N/200})\)
on smaller matching neighborhoods. The whole original forced
polynomial \(d_N\) and both Fourier coefficients entered the exact
physical residue identity before (21); neither is replaced here.

In particular the open lower-right minus upper-right difference is
still exactly
\[
\mathscr H_N(1/2)
 =\frac1{\kappa^2N}\phi_N[
       \mathcal R_N^3K_N^{\rm ord}(w,\cdot)
                    \mathcal I_{0,N}^{\rm mid}(\cdot,Z)]
   -V_N(1)+V_N(L_N)-J_N^{\rm grid}+\mathcal E_N,
\qquad L_N=(M_N-1/2)/N .                                     \tag{22}
\]
The seam and half-grid verticals and the possible even-level strip
are unchanged. The remaining coherent insertion has physical
indices \(N/2\le b<5N/6\); its norm or signed terminal observation
has not been paid. Equations (21)--(22) do not separately suppress
either original Fourier sector, nor identify a physical-node band
with an open contour arc. The statement is for the actual ordinary
next-three family \(m\ge5\), not terminal \(343\), length four,
or next own type four.
