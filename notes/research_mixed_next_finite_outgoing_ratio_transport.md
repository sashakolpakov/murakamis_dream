# Successive ratios of the complete finite outgoing sum

Private research proof, 8 November 2026. The selected outgoing action
can be recovered from ratios of the actual finite polynomials on the
physical middle interval. The proof uses the exact terminating
recurrence and a local comparison of its resolvent with a constant
half-line recurrence. It does not infer a finite asymptotic from a
principal characteristic alone.

This is a relative estimate. It does not determine the size of the
initial polynomial, the amplitude of the complete transfer, or the
cancellation in its remaining inner-period observation. No mathematical
numerical evaluation is used.

## 1. The finite sequence and the assertion

Keep the notation of the
[trailing determinant theorem](research_mixed_next_outgoing_trailing_determinants.md).
In particular,
\[
 D=N-1,\quad M=\lceil N/2\rceil,\quad L=\lfloor N/6\rfloor,
 \quad \theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},
 \quad s_b=2\sin(b\theta),\quad S_b=\prod_{j=1}^b s_j.
\]
The complete unsigned outgoing polynomial is
\[
 C_{b,N}(Z)=\sum_{k=0}^{D}
   \frac{(r^b)^{-k}(r^{b+1};r)_k(rZ;r)_k}{(r;r)_k^2}.
                                                               \tag{1}
\]
Here \((v;r)_k=\prod_{j=0}^{k-1}(1-vr^j)\), with the empty
product equal to one.
At a physical index \(0\le b\le D\), its literal upper stop is
\(D-b\). Thus (1) has no denominator \((r;r)_N\). The signed
sequence is \(a^{\rm all}_{b,N}=(-q)^b C_{b,N}\).

Use the parameter region
\[
 z_*=u+ih,\qquad 3/10\le u\le39/100,
 \qquad -3/100\le h\le1/50,\qquad Z=e^{-2\pi i z_*}.             \tag{2}
\]
The action \(\mathcal S(a,z_*)\) is the original zero-lift critical
value defined in the
[selected-sheet theorem](research_mixed_next_outer_selected_outgoing_sheet.md).
In particular it is not shifted by an additive normalization. On
\(1/2\le a\le5/6\), that theorem and the
[action-transport theorem](research_mixed_next_outgoing_selected_action_transport.md)
give
\[
 e^{\partial_a\mathcal S}=-z_{\rm per}^{-1},\qquad
 |z_{\rm per}|>\frac{126}{125}\sqrt{2\sin(\pi a)}.                \tag{3}
\]

**Theorem.** There is a constant \(C\), independent of the level,
the index, and (2), such that for all sufficiently large \(N\),
\[
 \frac{C_{b,N}(Z)}{C_{b-1,N}(Z)}
 =e^{\partial_a\mathcal S(b/N,z_*)}(1+\epsilon_{b,N}),
 \qquad |\epsilon_{b,N}|\le C/N,
 \qquad M\le b\le D-L.                                         \tag{4}
\]
Every denominator in (4) is nonzero. In particular, after increasing
the lower bound on \(N\),
\[
 \sqrt{s_b}\left|\frac{C_{b,N}(Z)}{C_{b-1,N}(Z)}\right|
 \le \frac{251}{252}.                                          \tag{5}
\]
There are constants \(0<c<C'<\infty\), uniform over (2), such that
\[
 c\,e^{N\Re\{\mathcal S(b/N,z_*)-\mathcal S(1/2,z_*)\}}
 \le \left|\frac{C_{b,N}(Z)}{C_{M-1,N}(Z)}\right|
 \le C'\,e^{N\Re\{\mathcal S(b/N,z_*)-\mathcal S(1/2,z_*)\}},
 \quad M\le b\le D-L.                                         \tag{6}
\]
Both parities are included. Formula (6) leaves the initial value
\(C_{M-1,N}\) in place.

## 2. The exact diagonal resolvent formula

Write
\[
 Y_b=r^b,\quad A_b=Y_b(Y_b-1),\quad
 B_b=3Y_b-(1+r)Y_b^2,\quad C_b^{\rm op}=r^{-1}(1-rY_b)^2.
\]
Here the superscript distinguishes the recurrence coefficient from
the polynomial in (1). For a trailing interval \(I_b=[b,D]\), let
\[
 G^{(b)}=(\mathcal J_{I_b,N}-ZI)^{-1},\qquad
 (\mathcal J_N f)_j=-qA_jf_{j-1}+B_jf_j-q^{-1}C_j^{\rm op}f_{j+1}.
\]
The trailing determinant theorem proves the exact identity
\[
 \frac{a^{\rm all}_{b,N}}{a^{\rm all}_{b-1,N}}
     =qA_b G^{(b)}_{b,b},                                      \tag{7}
\]
and nonvanishing of \(C_{b-1,N}\) for every \(M\le b\le D\).
It uses the original last row, where \(C_D^{\rm op}=0\), and the
actual terminal value \(a^{\rm all}_{D,N}=(-q)^D\).

Let \(K_b=\operatorname{diag}_{j\in I_b}(\sqrt{S_j})\), and retain
the row factor
\[
 w_j=\exp i\{(5j/2+1/4)\theta-\pi/4\},\qquad W_b=\operatorname{diag}(w_j).
\]
Define
\[
 H_{b,N}=W_b K_b(\mathcal J_{I_b,N}-ZI)K_b^{-1}.
                                                               \tag{8}
\]
The order in (8) matters. Since all displayed diagonal factors
commute with one another,
\[
 (H_{b,N}^{-1})_{0,0}=G^{(b)}_{b,b}/w_b,                         \tag{9}
\]
where the left side numbers \(I_b\) from zero. Its diagonal is
\[
 V_{j,N}=3e^{i(t_j+\theta/4)}
       +2\cos\theta\,e^{-i(3t_j+3\theta/4)}
       +\rho e^{i(5t_j+\theta/4-\alpha)},
 \qquad t_j=(j\theta-\pi/2)/2,\quad Z=\rho e^{-i\alpha}.
                                                               \tag{10}
\]
Its upper off-diagonal entry is
\[
 h_{j,N}=s_{j+1}^{3/2}e^{i(t_j-3\theta/4)},                       \tag{11}
\]
and its lower entry is the complex conjugate. Thus the off-diagonal
part is Hermitian, although the diagonal need not be real.

The full-tail energy proof, with the natural last row included as
in the trailing determinant theorem, gives constants \(C_0,\gamma>0\)
independent of \(N,b,Z\) such that
\[
 |(H_{b,N}^{-1})_{0,k}|\le C_0 e^{-\gamma k},
 \qquad 0\le k\le D-b.                                       \tag{12}
\]
The square-root sine products have already been included in (8);
there is no omitted metric factor in (12).

## 3. Freezing the coefficients at the left endpoint

For \(t=t_b\), put
\[
 \sigma=2\cos(2t)=s_b,\quad \tau=\sigma^{3/2},\quad
 V=3e^{it}+2e^{-3it}+Ze^{5it}.
\]
On \(\ell^2(\mathbb Z_{\ge0})\), define the bounded half-line operator
\[
 (H^0 f)_k=\tau e^{-it}f_{k-1}+Vf_k+\tau e^{it}f_{k+1},
 \qquad f_{-1}=0.                                             \tag{13}
\]
For the whole middle interval, the principal energy inequality is
\[
 \Re V-3\Im V-2\tau>51/350.                                   \tag{14}
\]
The off-diagonal part of (13) is self-adjoint. Consequently
\(\Re\langle f,(1+3i)H^0f\rangle\ge(51/350)\|f\|^2\).
This bounded-below inequality also holds for the adjoint of
\((1+3i)H^0\). Its range is closed and its orthogonal complement,
the adjoint kernel, is zero. Therefore \(H^0\) is invertible with a
uniform inverse norm. Set
\[
 m(t,Z)=((H^0)^{-1})_{0,0},\qquad f=(H^0)^{-1}\mathbf e_0.       \tag{15}
\]

We claim
\[
 (H_{b,N}^{-1})_{0,0}=m(t_b,Z)+O(N^{-1}),
                 \qquad M\le b\le D-L,                       \tag{16}
\]
uniformly over (2). Here is a direct proof retaining the distant
endpoint. Put \(n=D-b\) and restrict \(f\) to \(0,\ldots,n\).
The coefficients (10)--(11) differ from their frozen counterparts
in row \(k\) by at most \(C(k+1)/N\). To see this, use
\(|s_{j+1}-s_j|\le2\theta\), the bounded derivative of
\(x^{3/2}\) on \([0,2]\), and the bounded derivatives of the
trigonometric expressions on \(0\le t\le\pi/4\). These estimates
remain valid at the last row; no inverse sine occurs.

Since \(\|f\|_2\) is uniformly bounded, the residual
\[
 d=H_{b,N}(f|_{[0,n]})-\mathbf e_0
\]
satisfies
\[
 |d_k|\le C(k+1)/N+C\mathbf1_{\{k=n\}}.                        \tag{17}
\]
The last term accounts for the omitted frozen upper link
\(\tau e^{it}f_{n+1}\). Applying (12) before summing gives
\[
 \begin{split}
 |(H_{b,N}^{-1})_{0,0}-m|
 &\le \frac{C}{N}\sum_{k=0}^n(k+1)e^{-\gamma k}
                        +Ce^{-\gamma n}\\
 &\le C'/N+Ce^{-\gamma L}=O(N^{-1}).
 \end{split}                                                   \tag{18}
\]
The lower bound \(n\ge L=\lfloor N/6\rfloor\) is the reason
the terminal defect does not affect this local approximation.
This proves (16) without an asymptotic assumption on the finite
sequence.

## 4. Identifying the frozen root, including its sign

Conjugating (13) by \(f_k=e^{-ikt}g_k\) makes both off-diagonal
coefficients equal to \(\tau\). Its homogeneous characteristic is
\[
                  \tau\xi^2+V\xi+\tau=0.                       \tag{19}
\]
There are no roots on the unit circle: such a root would put
\(V\) in the real segment \([-2\tau,2\tau]\), contradicting
(14). The product of the roots is one. Thus exactly one root
has modulus less than one. The square-summable solution of the
inhomogeneous equation at zero gives
\[
 m=-\xi/\tau,\qquad \tau^2m^2-Vm+1=0,
                       \qquad |\tau m|<1.                     \tag{20}
\]
In particular \(m\ne0\). Continuous dependence of the bounded
inverse on the coefficients, on this compact parameter set,
gives a uniform positive lower bound for \(|m|\).

Set \(a=b/N\), \(Y=e^{-2\pi ia}\), and
\[
 A=Y(Y-1),\quad B=3Y-2Y^2,\quad C^{\rm op}=(1-Y)^2,
 \quad w=-e^{5it}.
\]
The limiting diagonal is \(V=w(B-Z)\), and direct multiplication
gives
\[
 |A|=\sigma,\qquad w^2 A C^{\rm op}=\sigma^3=\tau^2.            \tag{21}
\]
It follows from (20) that \(R=Awm\) satisfies
\[
 -A/R+B-Z-C^{\rm op}R=0,\qquad |R|<\sigma^{-1/2}.              \tag{22}
\]
The two signed outgoing roots have product \(A/C^{\rm op}\),
whose modulus is \(1/\sigma\). Thus (22) selects its unique
inside root. The selected-sheet theorem identifies that root as
\(R=z_{\rm per}^{-1}\), whereas the *unsigned* ratio is
\(-R=e^{\partial_a\mathcal S}\). The minus sign is essential.

Finally (7)--(9) give the exact unsigned ratio
\[
 \frac{C_{b,N}}{C_{b-1,N}}
       =-A_b w_b(H_{b,N}^{-1})_{0,0}.                           \tag{23}
\]
Here \(A_b=A\) exactly and \(w_b=w e^{i\theta/4}\).
Substituting (16), using the positive lower bound for \(|m|\),
and then (22) proves (4).

## 5. Relative action and finite decay

Equations (3)--(4) imply
\[
 \sqrt{s_b}|C_{b,N}/C_{b-1,N}|
    \le(125/126)(1+C/N).
\]
Since \(125/126=250/252<251/252\), this proves (5) for all
sufficiently large levels. Consequently the complete actual
sequence satisfies, for \(M-1\le b_0<b_1\le D-L\),
\[
 \sqrt{S_{b_1}/S_{b_0}}
 \left|C_{b_1,N}/C_{b_0,N}\right|
       \le(251/252)^{b_1-b_0}.                                \tag{24}
\]
This is a finite inequality, not just a comparison of critical
actions.

To prove (6), take real logarithms of the moduli in (4). The
error in each logarithm is \(O(1/N)\). The action derivative is
continuously differentiable, with a uniform derivative bound,
on the compact middle interval and parameter rectangle: the
selected root is simple and its logarithmic arguments stay
off their divisors. Therefore its Riemann sum satisfies
\[
 \sum_{j=M}^b\Re\partial_a\mathcal S(j/N,z_*)
   =N\Re\{\mathcal S(b/N,z_*)-\mathcal S(1/2,z_*)\}+O(1).
                                                               \tag{25}
\]
This also holds when the sum has only one term. The displacement
of its first index from \(N/2\), at either parity, costs \(O(1)\)
after multiplication by \(N\). Summing the logarithmic errors
costs another \(O(1)\). Exponentiating proves (6).

The conclusion does not give an absolute asymptotic for
\(C_{M-1,N}\). It also does not bound the coherent contraction
with the original inner periods. Those are distinct questions;
neither follows from (24), which concerns transport of the
outgoing sequence alone.

## Source versions

- Exact trailing determinants and natural last row:
  8564c705a0c8cd96cb7211c10166a522dde511bda27a94ac18a7cdafccf0b47f.
- Full-tail weighted energy:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Original selected outgoing sheet:
  850d97273259d39b0fc0ecf89bedaddceb97b13555c38a95d1f3e9fa7643067d.
- Quantitative selected action:
  77ffb14e6f3a3408b4aee3594d1c205b9db61fccdbf011181de9f86c26e9dbd5.

The author read back the full proof and the exact normalization
sources before freezing this version. No evaluation or replay was run.
